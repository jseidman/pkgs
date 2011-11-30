%define _topdir	 	/home/jseidman/protobuf
%define name	        protobuf 
%define release		1
%define version 	2.4.1
%define buildroot %{_topdir}/%{name}-%{version}-root

BuildRoot:	%{buildroot}
Summary: 	Google Protocol Buffers
License: 	GPL
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Prefix: 	/usr/local
Group: 		Development/Tools

%description

%prep
%setup -q

%build
./configure
make

%install
make install prefix=$RPM_BUILD_ROOT/usr/local

%files
%defattr(-,root,root)
/usr/local/lib
/usr/local/include/google/protobuf/
/usr/local/bin
