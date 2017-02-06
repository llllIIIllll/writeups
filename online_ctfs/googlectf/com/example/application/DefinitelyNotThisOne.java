package com.example.application;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;
import com.example.hellojni.Manifest.permission;
import com.example.hellojni.R;

public class DefinitelyNotThisOne extends Activity {
    public native String computeFlag(String str, String str2);

    public native String definitelyNotThis(String str, String str2);

    public native String orThat(String str, String str2, String str3);

    public native String perhapsThis(String str, String str2, String str3);

    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        new TextView(this).setText("Activity - Is_this_the_real_one");
        Button button = new Button(this);
        button.setText("Broadcast Intent");
        setContentView(button);
        button.setOnClickListener(new OnClickListener() {
            public void onClick(View v) {
                Intent intent = new Intent();
                intent.setAction("com.ctf.OUTGOING_INTENT");
                String a = DefinitelyNotThisOne.this.getResources().getString(R.string.str1);
                intent.putExtra("msg", DefinitelyNotThisOne.this.definitelyNotThis(Utilities.doBoth(DefinitelyNotThisOne.this.getResources().getString(R.string.test)), Utilities.doBoth("Test")));
                DefinitelyNotThisOne.this.sendBroadcast(intent, permission._MSG);
            }
        });
    }

    static {
        System.loadLibrary("hello-jni");
    }
}
