package com.example.application;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.widget.Toast;

public class Send_to_Activity extends BroadcastReceiver {
    public void onReceive(Context context, Intent intent) {
        String msgText = intent.getStringExtra("msg");
        if (msgText.equalsIgnoreCase("ThisIsTheRealOne")) {
            context.startActivity(new Intent(context, ThisIsTheRealOne.class));
        } else if (msgText.equalsIgnoreCase("IsThisTheRealOne")) {
            context.startActivity(new Intent(context, IsThisTheRealOne.class));
        } else if (msgText.equalsIgnoreCase("DefinitelyNotThisOne")) {
            context.startActivity(new Intent(context, DefinitelyNotThisOne.class));
        } else {
            Toast.makeText(context, "Which Activity do you wish to interact with?", 1).show();
        }
    }
}
