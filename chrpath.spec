#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : chrpath
Version  : 0.16
Release  : 5
URL      : https://alioth.debian.org/frs/download.php/latestfile/813/chrpath-0.16.tar.gz
Source0  : https://alioth.debian.org/frs/download.php/latestfile/813/chrpath-0.16.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: chrpath-bin
Requires: chrpath-doc

%description
chrpath
=======
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.  Eventually, I hope to be able to add an rpath if it is
missing.

%package bin
Summary: bin components for the chrpath package.
Group: Binaries

%description bin
bin components for the chrpath package.


%package doc
Summary: doc components for the chrpath package.
Group: Documentation

%description doc
doc components for the chrpath package.


%prep
%setup -q -n chrpath-0.16

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/doc/chrpath-0.16/AUTHORS
/usr/doc/chrpath-0.16/COPYING
/usr/doc/chrpath-0.16/ChangeLog
/usr/doc/chrpath-0.16/INSTALL
/usr/doc/chrpath-0.16/NEWS
/usr/doc/chrpath-0.16/README

%files bin
%defattr(-,root,root,-)
/usr/bin/chrpath

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
