import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Window

    RowLayout{
        id: controlRoot
        property string label: "none2"
        property string value: ""

        property string placeholderText: "Enter text"

        width: side
        TextField{
            id: textValueField
            placeholderText: "Enter text"
            onFocusChanged: {
                console.log("MyTest 2 Focus changed: ", activeFocus)
                if (activeFocus)
                    myPopup.open()
                else
                    myPopup.close()
            }

            Popup {
                id: myPopup
                x: textValueField.x
                y: textValueField.y + textValueField.height
                modal: true
                focus: true
                closePolicy: Popup.CloseOnEscape
                ColumnLayout{
                    Button{
                        text:" B1"
                    }
                    Button{
                        text: "button 2"
                    }
                    Button{
                        text: "button 333"
                    }
                }
            }
        }
    }
