#ifndef MY_HEADER_H
#define MY_HEADER_H
 
//These includes are required 
#include <QWidget>
#include <QVBoxLayout>
#include <QPushButton>
#include <QLabel>
#include <QTimer>

//QtGpio object derived from QWidget
class My_class : public QWidget
{
    Q_OBJECT     // Q_OBJECT macro is boilerplate. Must exist in all Qt applications
           
    public:
        My_class(); // QtGpio constructor...must take on a parent parameter that defaults to NULL
        ~My_class(); // QtGpio destructor
    public slots: // Slot Methods
        void btnStatus_1(void);
                
    private:      
        QPushButton *button_1, *button_2, *button_3; // We need two Buttons 
        QLabel *lblBtnState_1, *lblBtnState_2, *lblBtnState_3, *lblInputPinState; // two labels
        QVBoxLayout *vbox; // a vertical layout manager
        QHBoxLayout *hbox1, *hbox2;
        QTimer *timer; // a timer
                       
};
#endif 
