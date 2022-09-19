import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

    RowLayout{
        id: controlRoot
        property int side: 100
        property string label: "none"
        property string value: ""

        property string placeholderText: "Enter text"

        width: side

        Text {
            id: labelText
            text: controlRoot.label
        }

        Text{
            id: textValueField
            enabled: false
            text: getValue()
            Menu {
                id: textContextMenu
                y: labelText.height
                TextField{
                    id: textInput
                    placeholderText: controlRoot.placeholderText
                    selectByMouse: true
                    anchors.left: parent.left
                    anchors.top: parent.top
                    onAccepted: {
                        controlRoot.value = textInput.text
                        textContextMenu.close()
                    }
                }

                MenuItem { text: "Paste"}
                MenuItem { text: "Cut" }
                MenuItem { text: "Copy" }
                MenuItem { text: "Paste"}
                MenuItem { text: "Cut" }
                MenuItem { text: "Copy" }
                MenuItem { text: "Paste"}
            }

            function getValue(){
                if (value === "")
                {
                    return controlRoot.placeholderText
                }
                return value;
            }
        }
        MouseArea {
            anchors.fill: textValueField
            onClicked: {
                addToCombo("added runtime")
                textContextMenu.popup()
                textInput.forceActiveFocus()
            }
        }

        function addToCombo(str){
            console.log("adding to menu: ", str)
            var menuItem = Qt.createComponent("MenuItem.qml");
            menuItem.text = str

            console.log("check value: ", menuItem.text)
            textContextMenu.insertItem(menuItem)
        }
    }
