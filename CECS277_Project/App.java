package CECS277_Project;
//ONE SUBMISSION PUT NAME IN COMMENT SECTION OF DROPBOX

import java.awt.event.*;
import java.awt.*;
import java.io.File;
import java.io.IOException;
import javax.swing.*;

class App extends JFrame {

    private JPanel mainPanel, topPanel;
    private JDesktopPane desktopPane;
    private JMenuBar mb, statusBar;
    private JButton details, simple;
    private JComboBox<String> toolbarBox;
    private FileFrame ff;
    private App app;

    public App() {
        mainPanel = new JPanel();
        topPanel = new JPanel();
        mb = new JMenuBar();
        new JPanel();
        desktopPane = new JDesktopPane();
        statusBar = new JMenuBar();
        details = new JButton("Details");
        simple = new JButton("Simple");
        ff = new FileFrame(this, "C:\\", 0, 0);
        app = this;
    }

    public void go() {
        mainPanel.setLayout(new BorderLayout());
        this.setTitle("277 File Manager");
        buildMenuBar();
        buildToolbar();
        buildStatusBar("C:");
        mainPanel.add(topPanel, BorderLayout.NORTH);
        mainPanel.add(desktopPane, BorderLayout.CENTER);
        desktopPane.add(ff);
        this.add(mainPanel);
        this.setSize(800, 600);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setVisible(true);
    }

    private void buildMenuBar() {
        JMenu fileMenu, treeMenu, windowMenu, helpMenu;
        fileMenu = new JMenu("File");
        treeMenu = new JMenu("Tree");
        windowMenu = new JMenu("Window");
        helpMenu = new JMenu("Help");

        // from the File tab
        JMenuItem rename = new JMenuItem("Rename");
        rename.addActionListener(new RenameCopyAction());
        JMenuItem copy = new JMenuItem("Copy");
        copy.addActionListener(new RenameCopyAction());
        JMenuItem delete = new JMenuItem("Delete");
        delete.addActionListener(new DeleteAction());
        JMenuItem run = new JMenuItem("Run");
        run.addActionListener(new RunAction());
        JMenuItem exit = new JMenuItem("Exit");
        exit.addActionListener(new ExitAction());

        // from the Run tab
        JMenuItem expandBranch = new JMenuItem("Expand Branch");
        expandBranch.addActionListener(new ExpandBranchAction());
        JMenuItem collapseBranch = new JMenuItem("Collapse Branch");
        collapseBranch.addActionListener(new CollpaseBranchAction());

        // from the window tab
        JMenuItem New = new JMenuItem("New");
        New.addActionListener(new NewAction());
        JMenuItem cascade = new JMenuItem("Cascade");
        cascade.addActionListener(new CascadeAction());

        // from the help tab
        JMenuItem help = new JMenuItem("Help");
        // help.addActionListener(new HelpAction());
        JMenuItem about = new JMenuItem("About");
        about.addActionListener(new AboutAction());

        fileMenu.add(rename);
        fileMenu.add(copy);
        fileMenu.add(delete);
        fileMenu.add(run);
        fileMenu.add(exit);
        helpMenu.add(help);
        helpMenu.add(about);
        windowMenu.add(New);
        windowMenu.add(cascade);
        treeMenu.add(expandBranch);
        treeMenu.add(collapseBranch);

        mb.add(fileMenu);
        mb.add(treeMenu);
        mb.add(windowMenu);
        mb.add(helpMenu);
        this.setJMenuBar(mb);
    }

    private void buildToolbar() {
        File[] paths;
        paths = File.listRoots();
        String[] s1 = new String[paths.length];
        int i = 0;
        for (File path : paths) {
            s1[i] = path.toString();
            i++;
        }
        toolbarBox = new JComboBox<String>(s1);
        topPanel.add(toolbarBox);
        topPanel.add(details);
        topPanel.add(simple);
        toolbarBox.addActionListener(new toolbarBoxAction());
        details.addActionListener(new DetailsAction());
        simple.addActionListener(new SimpleAction());
    }

    public void buildStatusBar(String currentDrive) {
        statusBar.removeAll();
        File file = new File(currentDrive);
        if(file.exists()) {
            int freeSpace = (int) (file.getUsableSpace() / (1024 * 1024 * 1024));
            int totalSpace = (int) (file.getTotalSpace() / (1024 * 1024 * 1024));
            int usedSpace = totalSpace - freeSpace;

            JLabel status = new JLabel("Current Drive: " + currentDrive + " Free Space: " + freeSpace + "GB"
                    + " Used Space: " + usedSpace + "GB" + " Total Space: " + totalSpace + "GB");
            statusBar.add(status);
            mainPanel.add(statusBar, BorderLayout.SOUTH);
        }
        else {
            System.out.println(currentDrive);
        }
        mainPanel.revalidate();
    }



     private class toolbarBoxAction implements ActionListener{
        @Override
        public void actionPerformed(ActionEvent e){
             String s = (String) toolbarBox.getSelectedItem();
             System.out.println("you selected " + s);
             buildStatusBar(s);
            mainPanel.revalidate();
        }
     }


    //Action Listeners

    private class SimpleAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            if (ff.getRightPanel().getfileList() != null) {
                ff.getRightPanel().setShowDetails(false);
            }
        }
    }

    private class DetailsAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            if (ff.getRightPanel().getfileList() != null) {
                ff = (FileFrame) desktopPane.getSelectedFrame();
                ff.getRightPanel().setShowDetails(true);
            }
        }
    }

    private class RenameCopyAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            ff = (FileFrame) desktopPane.getSelectedFrame();
            DataBack dbdlg = new DataBack();
            dbdlg.setFileNameTextField(ff.getRightPanel().getFile().getPath());
            dbdlg.setDirectory(ff.getRightPanel().getFile().getParent());
            if (ff.getRightPanel().getfileList() != null) {
                if (e.getActionCommand().equals("Rename")){
                    dbdlg.setTitle("Rename!");
                    dbdlg.setVisible(true);
                    if(dbdlg.getRenameCopy()) {
                        String newFile = dbdlg.getFileNameTextField();
                        ff.getRightPanel().renameFile(newFile);
                    }
                }

                if (e.getActionCommand().equals("Copy")){
                    dbdlg.setTitle("Copy");
                    dbdlg.setVisible(true);
                    if(dbdlg.getRenameCopy()) {
                        ff.getRightPanel().setCopiedFile(ff.getRightPanel().getFile());
                        String newFile = dbdlg.getFileNameTextField();
                        try {
                            ff.getRightPanel().pasteFile(newFile);
                        } catch (IOException ioException) {
                            ioException.printStackTrace();
                        }
                        System.out.println("Copy File is set to: " + ff.getRightPanel().getCopiedFile().getName());
                    }
                }
            }
        }
    }

    private class DeleteAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            if (ff.getRightPanel().getfileList() != null) {
                ff = (FileFrame) desktopPane.getSelectedFrame();
                System.out.println("Delete: " + ff.getRightPanel().getFile());
                deleteDLG dlg = new deleteDLG();
                dlg.setTitle("Delete");
                dlg.setFileNameTextField(ff.getRightPanel().getFile().getPath());
                dlg.setVisible(true);
                if(dlg.getDelete())
                    ff.getRightPanel().deleteFile();
            }
        }
    }

    private class RunAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            if (ff.getRightPanel().getfileList() != null) {
                ff = (FileFrame) desktopPane.getSelectedFrame();
                ff.getRightPanel().runFile(ff.getRightPanel().getFile());
            }
        }
    }

    private class ExitAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            System.exit(0);
        }
    }

    private class ExpandBranchAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            ff.getLeftPanel().expandTree();

        }
    }

    private class CollpaseBranchAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            ff.getLeftPanel().collapseTree();
        }
    }

    private class NewAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String s = (String) toolbarBox.getSelectedItem();
            FileFrame ff = new FileFrame(app, s, 0, 100);
            desktopPane.add(ff);
        }
    }

    private class CascadeAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            JInternalFrame[] cascade = desktopPane.getAllFrames();
            int i = 10;
            int j = 10;
            for (JInternalFrame k : cascade) {
                k.setLocation(i, j);
                i += 25;
                j += 25;
                k.moveToFront();
            }
        }
    }

    private class AboutAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            Aboutdlg dlg = new Aboutdlg();
            dlg.setVisible(true);
        }
    }
}

