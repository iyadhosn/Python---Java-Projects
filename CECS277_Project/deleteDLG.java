package CECS277_Project;

import javax.swing.*;
import java.awt.event.*;


public class deleteDLG extends JDialog {
    private JPanel contentPane;
    private JButton buttonOK;
    private JButton buttonCancel;
    private JTextField fileNameTextField;
    private boolean delete;
    public deleteDLG() {
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

    public void setFileNameTextField(String s){
        fileNameTextField.setText(s);
    }

    public void onOK() {
        delete = true;
        dispose();
    }

    public void onCancel() {
        delete = false;
        dispose();
    }

    public boolean getDelete(){
        return delete;
    }
}
