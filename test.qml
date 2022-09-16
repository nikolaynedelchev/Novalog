import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow{
    title: qsTr("Hello  world")
    visible: true
    width: 400
    height: 400

    ColumnLayout{
        spacing: 2
        Button{
            text: qsTr("Click me")
            onClicked:{
                console.log("Hello from Qml")
                backend.printTxt()
                sashoId.enabled = false
            }
        }

        Button{
            text: qsTr("Show subpage")
            onClicked:{
                console.log("Sub page showing")
                subPage.openSubPage()
            }
        }
    }

    Connections{
        id: sashoId
        target: backend
        function onSignalPrintTxt_Sasho(boolValue){
            console.log("Hello from signal Sasho handler")
        }

        function foo(){
            console.log("test connection")
            enabled = false
        }
    }

//    JsonData {
//        id: jsonData;
//    }
    Connections{
        id: stdId
        target: backend
        function onSignalPrintTxt(boolValue, intValue, strValue, listValue, dictValue){

            var jd = JSON.parse(dictValue)

            //console.log("--- Hello from signal handler", boolValue, ", ", strVal, ", ", intVal)
            console.log("--- Hello from signal handler", boolValue, ", ", intValue, ", ", strValue, ", ", listValue[0], ", ",
                        jd.age)
        }
    }

    QtObject{
        id: subPage
        function openSubPage(){
            let component = Qt.createComponent("test_2.qml")
            let window = component.createObject()
            window.show()
            modality = true

            //visible = false
        }
    }
}
