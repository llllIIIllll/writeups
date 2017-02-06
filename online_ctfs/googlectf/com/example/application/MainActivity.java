package com.example.application;

import android.app.Activity;
import android.content.IntentFilter;
import android.os.Bundle;
import android.widget.TextView;
import com.example.hellojni.Manifest.permission;

public class MainActivity extends Activity {
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        TextView tv = new TextView(getApplicationContext());
        tv.setText("Select the activity you wish to interact with.To-Do: Add buttons to select activity, for now use Send_to_Activity");
        setContentView(tv);
        IntentFilter filter = new IntentFilter();
        filter.addAction("com.ctf.INCOMING_INTENT");
        registerReceiver(new Send_to_Activity(), filter, permission._MSG, null);
    }
}
