%define name itertools
%define version 0.1
%define release 1
%define _topdir %{_tmppath}/%{name}-%{version}-%{release}-root

Summary: Install the R itertools package.
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL-2
Group: Development/Libraries
BuildArch: x86_64
URL: http://cran.r-project.org/web/packages/itertools/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root/BUILD

%description
"Various tools for creating iterators, many patterned after functions in the 
Python itertools module, and others patterned after functions in the 'snow'
package."

%prep

%build

%install
R CMD INSTALL -l $RPM_BUILD_ROOT/usr/lib64/R/library %{_topdir}/SOURCES/%{name}_%{version}-1.tar.gz

%files
%defattr(-,root,root,-)
/usr/*
