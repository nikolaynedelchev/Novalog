import QtQuick
import QtQuick.Controls

ApplicationWindow{
    title: qsTr("2222 Hello  world 222 ")
    visible: true
    width: 300
    height: 300
    Button{
        text: qsTr("Click me 222")
        onClicked:{
            console.log("Hello 222 from Qml")
            backend.printTxt()
        }
    }

    Connections{
        id: sashoId
        target: backend
        function onSignalPrintTxt_Sasho(boolValue){
            console.log("Hello from signal Sasho handler")
        }
    }
}
