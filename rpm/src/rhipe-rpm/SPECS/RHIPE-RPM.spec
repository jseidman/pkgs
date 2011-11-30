%define name Rhipe
%define version 0.66
%define release 1
%define _topdir %{_tmppath}/%{name}-%{version}-%{release}-root

Summary: Install RHIPE and dependencies
Name: %{name}
Version: %{version}
Release: %{release}
License: Apache
Group: Development/Libraries
BuildArch: x86_64
URL: http://www.stat.purdue.edu/~sguha/rhipe/
BuildRoot: %{_topdir}/BUILD
Requires: protobuf, R-core

%description
A Java package that integrates R with Hadoop and facilitates implementing MapReduce in R.

%prep

%build

%install
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
export HADOOP=/usr/lib/hadoop-0.20
R CMD INSTALL -l $RPM_BUILD_ROOT/usr/lib64/R/library %{_topdir}/SOURCES/%{name}_%{version}.tar.gz

%files
%defattr(-,root,root,-)
/usr/*

