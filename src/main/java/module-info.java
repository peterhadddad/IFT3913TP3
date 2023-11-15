module tp3 {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.desktop;
    opens tp3 to javafx.fxml;
    exports tp3;
}