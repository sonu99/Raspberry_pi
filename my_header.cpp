#include "my_header.h"
bool state = false; 
My_class::My_class():QWidget()
{
    button_1 = new QPushButton("Button1");
    button_2 = new QPushButton("Button2");
    button_3 = new QPushButton("Button3");
    lblBtnState_1  = new QLabel("GPIO Default"); // instatiate labels
    lblBtnState_2  = new QLabel("GPIO Default"); // instatiate labels
    lblBtnState_3  = new QLabel("GPIO Default"); // instatiate labels

    lblInputPinState = new QLabel("Input pin value is : ?? ");
    vbox = new QVBoxLayout(); // instantiate layout manager
    hbox1 = new QHBoxLayout();
    hbox2 = new QHBoxLayout();
    timer = new QTimer(this); // instantiate timer....make timer child of the QtGpio class

    vbox->addWidget(lblInputPinState); // add all controls/widgets to layout manager
    hbox1->addWidget(button_1);
    hbox1->addWidget(button_2);
    hbox1->addWidget(button_3);

    hbox2->addWidget(lblBtnState_1);
    hbox2->addWidget(lblBtnState_2);
    hbox2->addWidget(lblBtnState_3);

    //this->setLayout(vbox); // set vbox as the window's (object's) layout manager
                           // this step also designates all controls (QPushButton, QLabel & QVBoxLayout) as children
                           // of the QtGpio class....
    this->setLayout(vbox);
    this->setLayout(hbox1);
    this->setLayout(hbox2);
    this->setWindowTitle("GUI for GPIO Toggling");   // Set window title 

    connect(button_1, SIGNAL(clicked()),this, SLOT(btnStatus_1()));//connect offBtn's clicked() signal to the btnOFF() slot method
    connect(button_2, SIGNAL(clicked()),this, SLOT(btnStatus_1()));//connect offBtn's clicked() signal to the btnOFF() slot method
    connect(button_3, SIGNAL(clicked()),this, SLOT(btnStatus_1()));//connect offBtn's clicked() signal to the btnOFF() slot method

    
    timer->start(250); // start timer. The timeout() signal is emitted every 250ms....therefor readInputPin slot method() runs once every 250ms
}

/**********************************************************************************************
 * Destructor - Since all references to Qt based controls/widgets are 'parented' either through 
 *              the layout manager or through pasing the  'this' pointer to their constructor
 *              we do not need to worry about deallocating their heap memory when they're done. 
 *              We do however need to worry about the memory of the rpiGpio object which is not 
 *              Qt based and not 'parented'
 * *******************************************************************************************/
My_class::~My_class(){
}

/********************************************************************************************
 * btnON() - slot method called whenever the onBtn button is pressed (see connect() 
 *           call in constructor). It sets GPIO4 to high..turning on the LED as well 
 *           as updating the text displayed by the lblBtnState_1 label
 *******************************************************************************************/

void My_class::btnStatus_1(void){

      
     state = !state;   
     if (state)
     {
         lblBtnState_1->setText("ON");
     }
     else
     { 
         lblBtnState_1->setText("OFF");
     }
}

