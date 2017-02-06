package com.example.application;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;
import com.example.hellojni.Manifest.permission;
import com.example.hellojni.R;

public class IsThisTheRealOne extends Activity {
    public native String computeFlag(String str, String str2);

    public native String definitelyNotThis(String str, String str2, String str3);

    public native String orThat(String str, String str2, String str3);

    public native String perhapsThis(String str, String str2, String str3);

    public void onCreate(Bundle savedInstanceState) {
        Context context = getApplicationContext();
        super.onCreate(savedInstanceState);
        new TextView(this).setText("Activity - Is_this_the_real_one");
        Button button = new Button(this);
        button.setText("Broadcast Intent");
        setContentView(button);
        button.setOnClickListener(new OnClickListener() {
            public void onClick(View v) {
                Intent intent = new Intent();
                intent.setAction("com.ctf.OUTGOING_INTENT");
                String a = IsThisTheRealOne.this.getResources().getString(R.string.str3) + "\\VlphgQbwvj~HuDgaeTzuSt.@Lex^~";
                String b = Utilities.doBoth(IsThisTheRealOne.this.getResources().getString(R.string.app_name));
                String name = getClass().getName();
                intent.putExtra("msg", IsThisTheRealOne.this.perhapsThis(a, b, Utilities.doBoth(name.substring(0, name.length() - 2))));
                IsThisTheRealOne.this.sendBroadcast(intent, permission._MSG);
            }
        });
    }

    static {
        System.loadLibrary("hello-jni");
    }
}
