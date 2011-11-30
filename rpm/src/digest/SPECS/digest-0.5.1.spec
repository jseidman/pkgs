%define name digest
%define version 0.5.1
%define release 1
%define _topdir %{_tmppath}/%{name}-%{version}-%{release}-root

Summary: Install the R digest package.
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL-2
Group: Development/Libraries
BuildArch: x86_64
URL: http://cran.r-project.org/web/packages/digest/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root/BUILD

%description
"Create cryptographic hash digests of R objects"

%prep

%build

%install
R CMD INSTALL -l $RPM_BUILD_ROOT/usr/lib64/R/library %{_topdir}/SOURCES/%{name}_%{version}.tar.gz

%files
%defattr(-,root,root,-)
/usr/*
