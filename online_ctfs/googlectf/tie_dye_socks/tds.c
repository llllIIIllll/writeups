#include <libmill.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <sys/types.h>
#include <fcntl.h>
#include <assert.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/wait.h>

struct request {
	uint32_t id;
	uint8_t op;
} __attribute__((packed));

struct prngctx { 
	uint32_t a, b, c, d;
};
#define rot(val, shft) (((val)<<(shft))|((val)>>(32-(shft))))


uint32_t prngnext(struct prngctx *c);
struct prngctx *prnginit(uint32_t seed);
void prngdone(struct prngctx *c);

struct prngctx *prnginit(uint32_t seed)
{
	struct prngctx *c;
	int i;

	c = malloc(sizeof(struct prngctx));
	if(c == NULL) return NULL;

	c->a = 0xabad1dea;
	c->b = seed - 0xc001d00d;
	c->c = seed + 0x5a5a5a5a;
	c->d = rot(seed, 29); 
	for(i = 0; i < 20; i++) prngnext(c);

	return c;
}


typedef enum {
	CMD_INVALID,
	CMD_PING,
	CMD_SITE,
	CMD_FLAG,
} command;

typedef struct msg {
	command cmd;
	uint8_t *buf;
	uint8_t *cmdbuf;
	size_t cmdlen;
	size_t len;
	size_t total;
} *msg_t;

struct chunk_data {
	 msg_t next;
};

msg_t msg_new(uint8_t *buf, size_t len);


void old_msg(msg_t m)
{
	if(m) {
		free(m->buf);
		free(m);
	}
}

coroutine void map_data(chan done, chan input, chan output, msg_t (*func)(void *data, msg_t), void *data)
{
	int cont = 1;
	msg_t d;

	while(cont == 1) {
		
		choose {
		in(done, int, i):
			cont = -1;
		in(input, msg_t, m):
			
			d = func(data, m);
			

			if(m == NULL) {
				cont = -1;
				break;
			}

			if(d) {
				
				chs(output, msg_t, d);
				break;
			}

			
			assert("why");
		end
		}
	}

	if(cont == 0) {
		// we're the first one to notice an error - exit.
		chdone(done, int, 1);
	}

	chclose(done);
	chdone(output, msg_t, NULL);
	chclose(output);
	chclose(input);
}

coroutine void map(chan done, chan input, chan output, msg_t (*func)(msg_t))
{
	int cont = 1;
	msg_t d;

	while(cont == 1) {
		
		choose {
		in(done, int, i):
			cont = -1;
		in(input, msg_t, m):
			

			if(m == NULL) {
				
				cont = -1;
				break;
			}

			

			d = func(m);

			

			if(d) {
				chs(output, msg_t, d);
				break;
			}

			
			cont = 0;
			assert("shouldn't happen");
			abort();
		end
		}
	}

	if(cont == 0) {
		// we're the first one to notice an error - exit.
		chdone(done, int, 1);
	}

	chclose(done);
	chdone(output, msg_t, NULL);
	chclose(output);
	chclose(input);
}

int strip_space(uint8_t **in, size_t *inlen, size_t *piecelen)
{
	uint8_t *p = *in;
	size_t i, j;

	

	j = *inlen;
	for(i = 0; i < j; i++) {
		
		if(p[i] == ' ') break;
		if(p[i] == 0) { break; }
	}

	if(i && p[i] != 0) {
		p[i] = 0;
	}



	*piecelen = i;
	*in = p + i + 1;
	*inlen = *inlen - i - 1;

	return 0;
} 

int parse(msg_t in)
{
	int state = 0;
	uint8_t *cur, *next;
	size_t i;
	size_t j;
	size_t remainder;
	uint8_t pbuf[] = { 'G', 'N', 'I', 'P' };
	uint8_t sbuf[] = { 'E', 'T', 'I', 'S' };
	uint8_t fbuf[] = { 'G', 'A', 'L', 'F' };
	int is_ping_cmd = 0;
	int is_site_cmd = 0;
	int is_flag_cmd = 0;

	

	cur = in->buf;
	remainder = in->len;

	strip_space(&cur, &remainder, &j);

	

	if(j == 0 || j > 4) {
		
		return -1;
	}

	for(i = 0; j <= 4 && i < j; i++) {
		
		is_ping_cmd |= pbuf[3 - i] ^ in->buf[i];
		is_site_cmd |= sbuf[3 - i] ^ in->buf[i];
		is_flag_cmd |= fbuf[3 - i] ^ in->buf[i];
		
		
		
	}

	// !!! just means it's super important.
	is_ping_cmd = !!!is_ping_cmd; 
	is_site_cmd = !!!is_site_cmd;
	is_flag_cmd = !!!is_flag_cmd;

	in->cmd = CMD_INVALID;

	if(is_ping_cmd) {
		in->cmd = CMD_PING;
		
	}

	if(is_site_cmd) {
		uint8_t *exec = cur;

		strip_space(&cur, &remainder, &j);
		

		if(j == 4 && exec[0] == 'E' && exec[1] == 'X' && exec[2] == 'E' && exec[3] == 'C') {
			
		}

		in->cmd = CMD_SITE;
		in->cmdbuf = cur;
		strip_space(&cur, &remainder, &j);
		
		in->cmdlen = j;
	} 

	if(is_flag_cmd) {
		uint8_t *please = cur;
		strip_space(&cur, &remainder, &j);
		
		if(j == 6 && please[0] == 'P' && please[1] == 'L' && please[2] == 'E' && please[3] == 'A' && please[4] == 'S' && please[5] == 'E') {
			in->cmd = CMD_FLAG;
		}
	}

	return 1;	
}

#define MAXSZ 1500

msg_t xor_func(void *data, msg_t in);

msg_t parse_func(msg_t in)
{
	int ok;

	ok = parse(in); 
	if(! ok) {
		old_msg(in);
		return NULL;	
	}

	return in;
}

msg_t cmd_invalid()
{
	msg_t ret;

	ret = msg_new((uint8_t *)"No such command available\x00", 26);
	return ret; 
}

msg_t cmd_pong(msg_t in)
{
	msg_t ret;

	
	
	ret = msg_new((uint8_t *)"PONG\x00", 5);
	return ret;
}

msg_t cmd_siteexec(msg_t in)
{
	msg_t out;
	size_t ret, off;

#define M "Command is unsupported - "
	
	char buf[4096];
	strcpy(buf, M);
	ret = in->cmdlen >= 4000 ? 4000 : in->cmdlen; 
	memcpy(buf + strlen(M), in->cmdbuf, ret);
	ret += strlen(M);
	buf[ret] = 0;

	
	out = msg_new(NULL, 4096);
	ret = snprintf((char *)out->buf, 4095, buf);
	out->len = ret;

	return out;
}

msg_t cmd_flag()
{
	msg_t out;

	out = msg_new((uint8_t *)FLAG, strlen(FLAG));
	return out;
}

msg_t cmd_func(msg_t in)
{
	int cont = 1;
	msg_t out;

	out = in;
	

	switch(in->cmd) {
		case CMD_INVALID:
			out = cmd_invalid();
			old_msg(in);
			break;
		case CMD_PING:
			out = cmd_pong(in);
			break;
		case CMD_SITE:
			out = cmd_siteexec(in);
			old_msg(in);
			break;
		case CMD_FLAG:
			out = cmd_flag();
			old_msg(in);
			break;
		default:
			assert("unhandled in->cmd");
	}

	
	return out;
		
}

coroutine void tcpreader(chan done, tcpsock sock, chan output)
{
	uint8_t buf[1500];
	size_t raw, sz;
	int i;
	int cont = 1;
	int64_t conn_deadline;
	int64_t read_deadline;
	msg_t msg;

	// XXX - refactor a little bit. we may wish to check if done has been called earlier..

	conn_deadline = now() + 5000;

	while(cont == 1) {
		
		choose {
		in(done, int, i):
			cont = -1;
		otherwise:
			read_deadline = now() + 150;
			msg = msg_new(NULL, MAXSZ);
			sz = tcprecv(sock, msg->buf, MAXSZ-1, read_deadline);
			
			if(errno && errno != ETIMEDOUT) {
				
				cont = 0;
				break;
			}

			if(sz == 0 && errno == ETIMEDOUT) {
				if(now() > conn_deadline) {
					cont = 0;
				}

				old_msg(msg);
				msg = NULL;
				break;
			}

			msg->len = sz;
			

			chs(output, msg_t, msg);
			conn_deadline = now() + 5000;
		end
		}
	}

	if(cont == 0) {
		// we're the first one to indicate we're finished..
		yield();
		choose {
		in(done, int, i):
			
		deadline(now() + 125):
			
			chdone(done, int, 1);
		end
		}
	}

	chclose(done);
	chdone(output, msg_t, NULL);
	chclose(output);
	tcpclose(sock);
}

coroutine void tcpwriter(chan done, chan input, tcpsock sock)
{
	int cont = 1;
	int64_t deadline;
	
	

	while(cont == 1) {
		

		choose {
		in(done, int, finished):
			
			cont = -1;
		in(input, msg_t, m):
			

			if(m == NULL) {
				// input closed
				cont = -1;
				break;
			}

			deadline = now() + 5000;

			tcpsend(sock, m->buf, m->len, deadline);
			tcpflush(sock, deadline);

			if(errno) {
				cont = 0;
				break;
			}

			old_msg(m);
		end
		}
	}

	if(cont == 0) {
		chs(done, int, 1);
	}
	
	chclose(done);
	chclose(input);
	// tcpreader() is responsible for tcpclose()'ing sock
}

coroutine static void filter_data(chan done, chan input, chan output, msg_t (*filter)(void *, msg_t), void *data)
{
	int cont = 1;
	msg_t d;

	while(cont == 1) {
		
		choose {
			in(done, int, i):
				
				cont = -1;
			in(input, msg_t, m):
				

				while((d = filter(data, m)) != NULL) {
					
					
					chs(output, msg_t, d);
				}				
				if(m == NULL) {
					cont = -1;
					break;
				}
				old_msg(m);
		end
		}
	}

	// no error conditions where we need to alert everyone else

	chclose(done);
	chclose(input);
	chclose(output);
}

void msg_append_data(msg_t m, uint8_t *buf, size_t len)
{
	size_t remainder = m->total - m->len;
	

	if(len > remainder) {
		size_t new;

		new = m->len + len + 256;

		m->buf = realloc(m->buf, new);
		if(m->buf == NULL) {
			abort();
		}
		m->total = new;
	}

	memcpy(m->buf + m->len, buf, len);
	m->len += len;

}

msg_t chunk_func(void *data, msg_t m)
{
	size_t i;
	struct chunk_data *cd = (struct chunk_data *)data;

	if(cd->next == NULL) cd->next = msg_new(NULL, 1024);

	

	for(i = 0; i < m->len; i++) {
		if(m->buf[i] == 0) {
			msg_t ret;
			

			ret = cd->next;
			cd->next = msg_new(NULL, 1024);
			msg_append_data(ret, m->buf, i);

			memmove(m->buf, m->buf + i + 1, m->len - i - 1);
			m->len -= i + 1;

			return ret;
		}
	}
	
	
	msg_append_data(cd->next, m->buf, m->len);

	return NULL;
}

coroutine void setup(tcpsock sock, uint32_t seed1, uint32_t seed2)
{
	struct prngctx *in, *out;
	struct chunk_data *cd;

	chan done;
	chan decrypt_in, chunk_in, parse_in, cmd_in;
	chan cmd_out, decrypt_out;	

	cd = calloc(1, sizeof(struct chunk_data));
	if(cd == NULL) { assert("blah"); abort(); }

	in = prnginit(seed1);
	out = prnginit(seed2);

#define Q 2

	done = chmake(int, 5);
	decrypt_in = chmake(msg_t, Q);
	chunk_in = chmake(msg_t, Q);
	parse_in = chmake(msg_t, Q);
	cmd_in = chmake(msg_t, Q);
	cmd_out = chmake(msg_t, Q);
	decrypt_out = chmake(msg_t, Q);

	go(tcpreader(done, sock, decrypt_in));	
	go(map_data(chdup(done), chdup(decrypt_in), chunk_in, xor_func, (void *)(in)));
	go(filter_data(chdup(done), chdup(chunk_in), parse_in, chunk_func, cd));
	go(map(chdup(done), chdup(parse_in), cmd_in, parse_func));
	go(map(chdup(done), chdup(cmd_in), cmd_out, cmd_func));
	go(map_data(chdup(done), chdup(cmd_out), decrypt_out, xor_func, (void *)(out)));
	go(tcpwriter(chdup(done), chdup(decrypt_out), sock)); 

}

uint32_t getseed(uint32_t *seed1, uint32_t *seed2)
{
	int fd;
	uint32_t ret;

	fd = open("/dev/urandom", O_RDONLY);
	if(fd == -1) {
		perror("open");
		exit(EXIT_FAILURE);
	}

	if(read(fd, seed1, sizeof(uint32_t)) != sizeof(uint32_t)) {
		perror("reading rand seed");
		exit(EXIT_FAILURE);
	}

	if(read(fd, seed2, sizeof(uint32_t)) != sizeof(uint32_t)) {
		perror("reading rand seed");
		exit(EXIT_FAILURE);
	}

	close(fd);

	return ret;
}

void selftest()
{
	// code you wish to test here ;)
}

#ifdef ADDR
void its_a_bad_idea(char *file)
{
	struct stat sb;
	int fd;
	size_t pgsz = sysconf(_SC_PAGESIZE);
	size_t mask = pgsz - 1;
	void *wanted = (void *)(ADDR & ~mask);

	void *m = mmap(wanted, pgsz*2, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0);

	if(m == MAP_FAILED) {
		
		
		exit(EXIT_FAILURE);
	}

	if(m != wanted) abort();

	if((fd = open(file, O_RDONLY)) == -1) {
		
		exit(EXIT_FAILURE);
	}

	if(read(fd, (void *)ADDR, mask - (ADDR & mask)) == -1) {
		
		exit(EXIT_FAILURE);
	}

	close(fd);
	mprotect(wanted, pgsz*2, PROT_READ);
}
#endif

static uint32_t overly_complicated(uint32_t a, uint32_t b, time_t c, pid_t d)
{
	uint32_t ret;

	ret = a + d;
	ret ^= (ret >> 16);
	ret += b;
	ret *= 0x85ebca6b;
	ret += c;
	ret ^= (ret >> 13);
	ret *= 0xc2b2ae35;
	ret ^= (ret >> 16);
	ret -= a;

	return ret;
}

static void looper(tcpsock s, uint32_t seed1, uint32_t seed2)
{
	srandom(overly_complicated(seed1, seed2, time(NULL), getpid()));

	while(1) {
		tcpsock c;
		c = tcpaccept(s, -1);
		if(! c) continue;

		go(setup(c, seed1, seed2));
	}
}

static void spinup(tcpsock s, uint32_t seed1, uint32_t seed2, int cnt)
{
	int i;

	for(i = 0; i < cnt; i++) {
		pid_t pid;
		pid = mfork();
		if(pid == 0) {
			looper(s, seed1, seed2);
			exit(EXIT_SUCCESS);
		}

		if(pid < 0) {
			// error state
			
			perror("mfork");
			exit(EXIT_FAILURE);
		}
	}	
}

int main(int argc, char **argv, char *envp)
{
	int port = 54320;
	ipaddr a;
	tcpsock s;
	uint32_t seed1, seed2;
	time_t n;
	int nproc;
	char *t;
	int i;

	// gotrace(1);

	if(argc > 1) {
		if(strcmp(argv[1], "--self-test") == 0) {
			selftest();
			exit(EXIT_FAILURE);
		}

		port = atoi(argv[1]);
	}

	getseed(&seed1, &seed2);
#ifdef ADDR
	its_a_bad_idea(KEYFILE);
#endif
	if(argc > 2) {
		seed1 = atoi(argv[2]);
	}

	if(argc > 3) {
		seed2 = atoi(argv[3]);
	}

	n = time(NULL);
	srandom(n);
	

	a = iplocal(NULL, port, 0);
	s = tcplisten(a, -1);
	if(! s) {
		perror("tcplisten");
		return -1;
	}

	t = getenv("NPROC");
	if(t == NULL) t = "1";
	nproc = atoi(t);

	spinup(s, seed1, seed2, nproc);

	while(1) {
		pid_t pid;
		int status;

		

		pid = waitpid(-1, &status, 0);
		if(pid > 0 && (WIFEXITED(status) || WIFSIGNALED(status))) {
			
			spinup(s, seed1, seed2, 1);
		}
	}

}

void prngdone(struct prngctx *c)
{
	if(c) {
		memset(c, 0, sizeof(struct prngctx));
		free(c);
	}
}

msg_t xor_func(void *data, msg_t in)
{
	struct prngctx *c = (struct prngctx *)(data);
	size_t i;

	

	if(in == NULL) {
		// last time this function will be called, so clean up data
		prngdone(c);
		return NULL;
	}

	for(i = 0; i < in->len; i++) {
		in->buf[i] ^= prngnext(data);
	}

	

	return in;
}



uint32_t prngnext(struct prngctx *c)
{
	uint32_t e;
	e = c->a + rot(c->b, 27);
	c->a = c->b - rot(c->c, 17);
	c->b = c->c ^ c->d;
	c->c = c->d - e;
	c->d = e + rot(e + c->a, 3);
	return c->d;
}


msg_t msg_new(uint8_t *buf, size_t len)
{
	msg_t ret;

	ret = calloc(1, sizeof(struct msg));
	if(len == 0) return ret;
	ret->total = len;

	ret->buf = calloc(1, len);
	if(ret->buf == NULL) {
		free(ret);
		return NULL;
	}

	if(buf == NULL) return ret;
	ret->len = len;
	memcpy(ret->buf, buf, len);
	return ret;
}


