%define name rmr
%define version 1.1
%define release 1
%define _topdir %{_tmppath}/%{name}-%{version}-%{release}-root

Summary: Install the rmr package, part of the Revolution Analytics RHadoop project
Name: %{name}
Version: %{version}
Release: %{release}
License: Apache
Group: Development/Libraries
BuildArch: x86_64
URL: https://github.com/RevolutionAnalytics/RHadoop/wiki/rmr
BuildRoot: %{_topdir}/BUILD

%description
An R package which provides an interface to Hadoop MapReduce development through the R environment.

%prep

%build

%install
R CMD INSTALL -l $RPM_BUILD_ROOT/usr/lib64/R/library %{_topdir}/SOURCES/%{name}_%{version}.tar.gz

%files
%defattr(-,root,root,-)
/usr/*
