#include <QApplication>
#include "my_header.h"
 
int main(int argc, char **argv)
{
    QApplication app (argc, argv);
 
    My_class my_application ;

    my_application.show();
 
    return app.exec();
}
