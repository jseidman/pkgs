%define name iterators
%define version 1.0.5
%define release 1
%define _topdir %{_tmppath}/%{name}-%{version}-%{release}-root

Summary: Install the R iterator package.
Name: %{name}
Version: %{version}
Release: %{release}
License: BSD
Group: Development/Libraries
BuildArch: x86_64
URL: http://cran.r-project.org/web/packages/iterators/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root/BUILD

%description
"Support for iterators, which allow a programmer to traverse through all the 
elements of a vector, list, or other collection of data."

%prep

%build

%install
R CMD INSTALL -l $RPM_BUILD_ROOT/usr/lib64/R/library %{_topdir}/SOURCES/%{name}_%{version}.tar.gz

%files
%defattr(-,root,root,-)
/usr/*
