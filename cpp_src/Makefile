all: main core/libcore.a app/libapp.a

main: main.cpp core/libcore.a app/libapp.a
	g++ -o main main.cpp core/libcore.a app/libapp.a

core/libcore.a: core/core.cpp core/core.h
	g++ -c core/core.cpp -o core/core.o -I.
	ar rvs core/libcore.a core/core.o

app/libapp.a: app/app.cpp app/app.h core/core.h core/core.cpp
	g++ -c app/app.cpp -o app/app.o -I.
	ar rvs app/libapp.a app/app.o
	
clean:
	rm -f core/core.o app/app.o core/libcore.a app/libapp.a main
