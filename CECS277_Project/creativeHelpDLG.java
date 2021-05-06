package CECS277_Project;

import javax.swing.*;
import java.awt.event.*;

public class creativeHelpDLG extends JDialog {
    private JPanel contentPane;
    private JButton buttonOK;
    private JTextField httpsWwwYoutubeComTextField;

    public creativeHelpDLG() {
        setContentPane(contentPane);
        setModal(true);
        getRootPane().setDefaultButton(buttonOK);
        this.setSize(400, 200);
        buttonOK.addActionListener(new okAction() {
            public void actionPerformed(ActionEvent e) {
                onOK();
            }
        });
    }

    private void onOK() {
        dispose();
    }


}
