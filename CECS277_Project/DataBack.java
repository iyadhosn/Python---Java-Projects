package CECS277_Project;

import javax.swing.*;
import java.awt.event.*;

public class DataBack extends JDialog {
    private JPanel contentPane;
    private JButton buttonOK;
    private JButton buttonCancel;
    private JTextField textField1;
    private JTextField textField2;
    private JTextField textField3;

    private boolean rename;


    public DataBack() {
        setContentPane(contentPane);
        setModal(true);
        getRootPane().setDefaultButton(buttonOK);
        this.setSize(400, 200);
        buttonOK.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                onOK();
            }
        });

        buttonCancel.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                onCancel();
            }
        });



    }
    public void setDirectory(String s){
        textField3.setText(s);
    }

    public void setFileNameTextField(String s){
       textField1.setText(s);
    }

    public String getFileNameTextField(){
        return textField2.getText();
    }
    public void onOK() {
        rename = true;
        dispose();
    }

    public void onCancel() {
        rename = false;
        dispose();
    }

    public boolean getRenameCopy(){
        return rename;
    }
}
