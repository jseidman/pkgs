%define name RJSONIO
%define version 0.96
%define release 1
%define _topdir %{_tmppath}/%{name}-%{version}-%{release}-root

Summary: Install the RJSONIO package, which provides access to JSON objects from R.
Name: %{name}
Version: %{version}
Release: %{release}
License: BSD
Group: Development/Libraries
BuildArch: x86_64
URL: http://cran.r-project.org/web/packages/RJSONIO/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root/BUILD

%description
An R package providing functionality to convert to and from JSON objects.

%prep

%build

%install
R CMD INSTALL -l $RPM_BUILD_ROOT/usr/lib64/R/library %{_topdir}/SOURCES/%{name}_%{version}-0.tar.gz

%files
%defattr(-,root,root,-)
/usr/*
