__Towers of Toast__
===========

_John Hammond_ | _Saturday, December 2nd, 2016_ 

 
> Everyone loves the Tower of Hanoi puzzle. Well it appears the Toaster Bot wants you to play an essentially identical game called "Towers of Toast". The game doesn't seem to be working though... Can you win anyway? Perhaps by loading a winning saved game? Download the Java code here. 


----------

This challenge is under the "[Reverse Engineering]" category, though it gives us [Java] source code, so I suppose it is not really the classical "[reverse engineering]" that we are used to. That's fine; it was an interesting challenge.

So I solved this just by kind of poking at it and reading the source code for a bit. That's really all we have to work with.

You can download the [Java] code [`Main.java`](Main.java) and you can read through it and all. It's quite wordy, but you make sense of it quickly.

The program is based off of the [Towers of Hanoi] math game or puzzle. If you don't know of it, I suggest you read up on it just briefly to get a basic idea -- or you can take my explanation and leave it at that. 

The game sets up a scenario where there are many different size disks on three poles (the _towers_). The objective of the game is to get ALL of the disks, in size order, on only _one_ of the towers. The rules of the game are that you can only move one disk at a time, you can only move the disk to another pole, and no disk can be put on top of a smaller disk.

I'm sure you can see how the game gets complex kind of quickly. 

The challenge prompt tells us that the program is seemingly not working... but the source code looks fine. Can we try and run it anyway?

You can "compile" and run [Java] code like so:

```
javac Main.java
java Main
```

You should be greeted with the game:

```
Welcome to Towers of Toast!!!
Type 'new' to start a new random puzzle
Type 'load' to load a saved puzzle

```

So the game gives us instructions to just enter `new` for a new game or `load` to load a new one. 

The challenge prompt had hinted that we could possibly win somehow, by loading a winning saved game. That must be our objective. 

I would hope at this point you have looked over some of the source code -- and I had, at this point, too -- but I still wasn't really certain what the game _did_ or how it saved the poles. So just for experiments sake let's try and run a new game.

```
Sorry the game is broken! :(
We saved your game, though. Here are your save game numbers:
39760838917665965165
9356823422485014
447780012957734102287931847716041

```

It spit out some pictures of the towers and some numbers that it apparently saved. These must be the "save poles" that they want when you load a game, you can see some of that in the source code.

If you look at the source code, you can see when you `load` a new game, it checks to see if your entries are valid. If your entries set you up to win, you get the flag:

``` java

public static void main(String[] args) {            
    Scanner inputter = new Scanner(System.in);

    System.out.println("Welcome to Towers of Toast!!!");
    System.out.println("Type 'new' to start a new random puzzle");
    System.out.println("Type 'load' to load a saved puzzle");
    String choice = inputter.nextLine();
    if (choice.equals("load")) {
        System.out.println("Enter save number for pole 1:");
        BigInteger pole1 = new BigInteger(inputter.nextLine());
        System.out.println("Enter save number for pole 2:");
        BigInteger pole2 = new BigInteger(inputter.nextLine());
        System.out.println("Enter save number for pole 3:");
        BigInteger pole3 = new BigInteger(inputter.nextLine());

        ArrayList<BigInteger> diskValues1 = readSavedPoleInformation(pole1);
        ArrayList<BigInteger> diskValues2 = readSavedPoleInformation(pole2);
        ArrayList<BigInteger> diskValues3 = readSavedPoleInformation(pole3);

        // Check that no disk appears on more than one pole
        HashSet<BigInteger> diskset1 = new HashSet<BigInteger>(diskValues1);
        HashSet<BigInteger> diskset2 = new HashSet<BigInteger>(diskValues2);
        HashSet<BigInteger> diskset3 = new HashSet<BigInteger>(diskValues3);
        if (!distinctSets(diskset1, diskset2) ||
                !distinctSets(diskset2, diskset3) || 
                !distinctSets(diskset1, diskset3)) {
            throw new RuntimeException("Prime can only appear in one pole value");
        }

        // Check that disks of all sizes are present
        if (diskValues1.size() + diskValues2.size() + diskValues3.size() < GAME_SIZE) {
            throw new RuntimeException("Not all disks accounted for");
        }

        // Display the picture of the situation
        printPoles(diskValues1, diskValues2, diskValues3);
        
        // Have we won?
        checkVictory(diskValues1, diskValues2, diskValues3);
    }

// ...
}
```

See that `checkVictory` function call at the very end? How does that work, exactly?

``` java
// You've won the game if all the disks are on a single pole
public static void checkVictory(ArrayList<BigInteger> pole1, ArrayList<BigInteger> pole2, ArrayList<BigInteger> pole3) {
    if (pole1.size() == GAME_SIZE || pole2.size() == GAME_SIZE || pole3.size() == GAME_SIZE) {
        BigInteger flag = createSavedPoleInformation(pole1).max(createSavedPoleInformation(pole2).max(createSavedPoleInformation(pole3)));          
        System.out.println("YOU WIN!");
        System.out.println("Your flag is: " + flag);
    }
}
```

Okay, so that creates the flag with some `createSavedPoleInformation` function, and it looks like it takes the `max` of those?

``` java
// Export information about disks on a given pole into a single large number.
// NOTE: Regular integers are far too big for this number, we need BigIntegers instead
public static BigInteger createSavedPoleInformation(ArrayList<BigInteger> disk) {
    ArrayList<BigInteger> primes = getPrimes(GAME_SIZE);
    BigInteger poleValue = BigInteger.ONE; // Start with one
    for (BigInteger i : disk) {
        // If a disk is size n, multiply by the nth prime number
        poleValue = poleValue.multiply(primes.get(i.intValue()));
    }   
    return poleValue;
}
```


Hmmm. Okay, so I initially thought that it wanted some "max" number, like it would check to see if one pole had the largest number. So, I tried to like zero out some other poles and I just chose the largest number from the previous game:

```
Welcome to Towers of Toast!!!
Type 'new' to start a new random puzzle
Type 'load' to load a saved puzzle
load
Enter save number for pole 1:
0
Enter save number for pole 2:
447780012957734102287931847716041
Enter save number for pole 3:
0
Exception in thread "main" java.lang.RuntimeException: Pole value 0 is no good. Each factor can only appear once in the pole number. Only the first 40 primes are allowed. No 0s.
    at Main.readSavedPoleInformation(Main.java:50)
    at Main.main(Main.java:84)

```

Oh! We broke it! We got this exception... `Pole value 0 is no good`, and `No 0s`. Oh, okay. So we can't use zeros. I'll try again, but with a smaller prime, like one or something...

```
Welcome to Towers of Toast!!!
Type 'new' to start a new random puzzle
Type 'load' to load a saved puzzle
load
Enter save number for pole 1:
1
Enter save number for pole 2:
1
Enter save number for pole 3:
447780012957734102287931847716041
Exception in thread "main" java.lang.RuntimeException: Not all disks accounted for
    at Main.main(Main.java:100)
```

Another exception... "Not all disks accounted for"? Where is that in the source code? 

I just did a little `Ctrl+F`:

``` java
// Check that disks of all sizes are present
if (diskValues1.size() + diskValues2.size() + diskValues3.size() < GAME_SIZE) {
    throw new RuntimeException("Not all disks accounted for");
}
```


Hmm. It's like adding all their sizes together. Is that what it is looking for? Let's add up all the numbers we got when we ran the game the first time.

``` python
>>> 39760838917665965165 + 9356823422485014 + 447780012957734102287931847716041
447780012957773872483672936166220L
```

[Python] knows it is a large number so it tacks that `L` on at the very end. Make sure to remove that when you are working with the number. 

Here we go, I'll try again:

```
Welcome to Towers of Toast!!!
Type 'new' to start a new random puzzle
Type 'load' to load a saved puzzle
load
Enter save number for pole 1:
447780012957773872483672936166220 
Enter save number for pole 2:
1
Enter save number for pole 3:
1
Exception in thread "main" java.lang.RuntimeException: Pole value 447780012957773872483672936166220 is no good. Each factor can only appear once in the pole number. Only the first 40 primes are allowed. No 0s.
    at Main.readSavedPoleInformation(Main.java:50)
    at Main.main(Main.java:84)
```

Damn, an exception again! The same one we saw before. But why...?

```
Pole value 447780012957773872483672936166220 is no good. Each factor can only appear once in the pole number. Only the first 40 primes are allowed. No 0s.
```

___OH! WAIT!___ These numbers are supposed to be factors, right?? What if rather than _adding_ them, we _MULTIPLY_ them?

``` python
>>> 39760838917665965165 * 9356823422485014 * 447780012957734102287931847716041
166589903787325219380851695350896256250980509594874862046961683989710L
```

Can we try this number?

```
Welcome to Towers of Toast!!!
Type 'new' to start a new random puzzle
Type 'load' to load a saved puzzle
load
Enter save number for pole 1:
166589903787325219380851695350896256250980509594874862046961683989710 
Enter save number for pole 2:
1
Enter save number for pole 3:
1
```

And it spits out a giant tower...

```
YOU WIN!
Your flag is: 166589903787325219380851695350896256250980509594874862046961683989710
```

_And hey, we got it!_

Sweet. This problem could have been solved without as much detective work and just thinking about the source code, but there was a lot to it and I just didn't want to go through it all. I'd rather poke at the program and cross-check with what happens.

__Submit: `166589903787325219380851695350896256250980509594874862046961683989710`__

[netcat]: https://en.wikipedia.org/wiki/Netcat
[Wikipedia]: https://www.wikipedia.org/
[Linux]: https://www.linux.com/
[man page]: https://en.wikipedia.org/wiki/Man_page
[PuTTY]: http://www.putty.org/
[ssh]: https://en.wikipedia.org/wiki/Secure_Shell
[Windows]: http://www.microsoft.com/en-us/windows
[virtual machine]: https://en.wikipedia.org/wiki/Virtual_machine
[operating system]:https://en.wikipedia.org/wiki/Operating_system
[OS]: https://en.wikipedia.org/wiki/Operating_system
[VMWare]: http://www.vmware.com/
[VirtualBox]: https://www.virtualbox.org/
[hostname]: https://en.wikipedia.org/wiki/Hostname
[port number]: https://en.wikipedia.org/wiki/Port_%28computer_networking%29
[distribution]:https://en.wikipedia.org/wiki/Linux_distribution
[Ubuntu]: http://www.ubuntu.com/
[ISO]: https://en.wikipedia.org/wiki/ISO_image
[standard streams]: https://en.wikipedia.org/wiki/Standard_streams
[read]: http://ss64.com/bash/read.html
[variable]: https://en.wikipedia.org/wiki/Variable_%28computer_science%29
[command substitution]: http://www.tldp.org/LDP/abs/html/commandsub.html
[permissions]: https://en.wikipedia.org/wiki/File_system_permissions
[redirection]: http://www.tldp.org/LDP/abs/html/io-redirection.html
[tmp]: http://www.tldp.org/LDP/Linux-Filesystem-Hierarchy/html/tmp.html
[curl]: http://curl.haxx.se/
[cl1p.net]: https://cl1p.net/
[request]: http://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html
[POST request]: https://en.wikipedia.org/wiki/POST_%28HTTP%29
[Python]: http://python.org/
[interpreter]: https://en.wikipedia.org/wiki/List_of_command-line_interpreters
[requests]: http://docs.python-requests.org/en/latest/
[urllib]: https://docs.python.org/2/library/urllib.html
[file handling with Python]: https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
[bash]: https://www.gnu.org/software/bash/
[Assembly]: https://en.wikipedia.org/wiki/Assembly_language
[the stack]:  https://en.wikipedia.org/wiki/Stack_%28abstract_data_type%29
[register]: http://www.tutorialspoint.com/assembly_programming/assembly_registers.htm
[hex]: https://en.wikipedia.org/wiki/Hexadecimal
[archive file]: https://en.wikipedia.org/wiki/Archive_file
[zip file]: https://en.wikipedia.org/wiki/Zip_%28file_format%29
[gigabytes]: https://en.wikipedia.org/wiki/Gigabyte
[GB]: https://en.wikipedia.org/wiki/Gigabyte
[GUI]: https://en.wikipedia.org/wiki/Graphical_user_interface
[Wireshark]: https://www.wireshark.org/
[FTP]: https://en.wikipedia.org/wiki/File_Transfer_Protocol
[client and server]: https://simple.wikipedia.org/wiki/Client-server
[RETR]: http://cr.yp.to/ftp/retr.html
[FTP server]: https://help.ubuntu.com/lts/serverguide/ftp-server.html
[SFTP]: https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol
[SSL]: https://en.wikipedia.org/wiki/Transport_Layer_Security
[encryption]: https://en.wikipedia.org/wiki/Encryption
[HTML]: https://en.wikipedia.org/wiki/HTML
[Flask]: http://flask.pocoo.org/
[SQL]: https://en.wikipedia.org/wiki/SQL
[and]: https://en.wikipedia.org/wiki/Logical_conjunction
[Cyberstakes]: https://cyberstakesonline.com/
[cat]: https://en.wikipedia.org/wiki/Cat_%28Unix%29
[symbolic link]: https://en.wikipedia.org/wiki/Symbolic_link
[ln]: https://en.wikipedia.org/wiki/Ln_%28Unix%29
[absolute path]: https://en.wikipedia.org/wiki/Path_%28computing%29
[CTF]: https://en.wikipedia.org/wiki/Capture_the_flag#Computer_security
[Cyberstakes]: https://cyberstakesonline.com/
[OverTheWire]: http://overthewire.org/
[Leviathan]: http://overthewire.org/wargames/leviathan/
[ls]: https://en.wikipedia.org/wiki/Ls
[grep]: https://en.wikipedia.org/wiki/Grep
[strings]: http://linux.die.net/man/1/strings
[ltrace]: http://linux.die.net/man/1/ltrace
[C]: https://en.wikipedia.org/wiki/C_%28programming_language%29
[strcmp]: http://linux.die.net/man/3/strcmp
[access]: http://pubs.opengroup.org/onlinepubs/009695399/functions/access.html
[system]: http://linux.die.net/man/3/system
[real user ID]: https://en.wikipedia.org/wiki/User_identifier
[effective user ID]: https://en.wikipedia.org/wiki/User_identifier
[brute force]: https://en.wikipedia.org/wiki/Brute-force_attack
[for loop]: https://en.wikipedia.org/wiki/For_loop
[bash programming]: http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html
[Behemoth]: http://overthewire.org/wargames/behemoth/
[command line]: https://en.wikipedia.org/wiki/Command-line_interface
[command-line]: https://en.wikipedia.org/wiki/Command-line_interface
[cli]: https://en.wikipedia.org/wiki/Command-line_interface
[PHP]: https://php.net/
[URL]: https://en.wikipedia.org/wiki/Uniform_Resource_Locator
[TamperData]: https://addons.mozilla.org/en-US/firefox/addon/tamper-data/
[Firefox]: https://www.mozilla.org/en-US/firefox/new/?product=firefox-3.6.8&os=osx%E2%8C%A9=en-US
[Caesar Cipher]: https://en.wikipedia.org/wiki/Caesar_cipher
[Google Reverse Image Search]: https://www.google.com/imghp
[PicoCTF]: https://picoctf.com/
[JavaScript]: https://www.javascript.com/
[base64]: https://en.wikipedia.org/wiki/Base64
[client-side]: https://en.wikipedia.org/wiki/Client-side_scripting
[client side]: https://en.wikipedia.org/wiki/Client-side_scripting
[javascript:alert]: http://www.w3schools.com/js/js_popup.asp
[Java]: https://www.java.com/en/
[2147483647]: https://en.wikipedia.org/wiki/2147483647_%28number%29
[XOR]: https://en.wikipedia.org/wiki/Exclusive_or
[XOR cipher]: https://en.wikipedia.org/wiki/XOR_cipher
[RSA]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
[Cryptography]: https://en.wikipedia.org/wiki/Cryptography
[private key]: https://en.wikipedia.org/wiki/Public-key_cryptography
[public key]: https://en.wikipedia.org/wiki/Public-key_cryptography
[reverse engineering]: https://en.wikipedia.org/wiki/Reverse_engineering
[Towers of Hanoi]: https://en.wikipedia.org/wiki/Tower_of_Hanoi