%define ver      0.9.0pre1
%define rel      rc4
%define prefix   /usr

Summary: Genealogical Research and Analysis Management Programming System.
Name: gramps
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/Genealogy
Source: http://download.sourceforge.net/gramps/gramps-%{ver}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-root

URL: http://gramps.sourceforge.net

Requires: python >= 1.5.2
Requires: pygnome >= 1.0.53
Requires: _gladegnomemodule.so
Requires: pyexpat.so

BuildRequires: scrollkeeper >= 0.1.4
BuildRequires: automake >= 1.6
BuildRequires: autoconf >= 2.52

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python
based plugin system.

%prep
%setup

%build
if [ ! -f configure ]; then
  CFLAGS="$MYCFLAGS" ./autogen.sh $MYARCH_FLAGS --prefix=%prefix
else
  CFLAGS="$MYCFLAGS" ./configure $MYARCH_FLAGS --prefix=%prefix
fi

make


%install
rm -rf $RPM_BUILD_ROOT

make GNOME_DATADIR=$RPM_BUILD_ROOT%{prefix}/share prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc README COPYING TODO INSTALL

%{prefix}/bin/gramps

%{_datadir}/gnome/help/gramps-manual/C/*
%{_datadir}/gnome/help/extending-gramps/C/*

%{_datadir}/gnome/apps/Applications/gramps.desktop
%{_datadir}/pixmaps/gramps.png
%{_datadir}/locale/*/LC_MESSAGES/gramps.mo

%{_datadir}/gramps/*.xpm
%{_datadir}/gramps/*.jpg
%{_datadir}/gramps/*.png
%{_datadir}/gramps/*.py
%{_datadir}/gramps/*.pyo
%{_datadir}/gramps/*.glade
%{_datadir}/gramps/*.so
%{_datadir}/gramps/docgen/*.py
%{_datadir}/gramps/docgen/*.pyo
%{_datadir}/gramps/filters/*.py
%{_datadir}/gramps/filters/*.pyo
%{_datadir}/gramps/plugins/*.py
%{_datadir}/gramps/plugins/*.pyo
%{_datadir}/gramps/plugins/*.glade
%{_datadir}/gramps/data/gedcom.xml
%{_datadir}/gramps/data/templates/*.tpkg
%{_datadir}/gramps/data/templates/*.xml

%{prefix}/man/man1/gramps.1*

%{_datadir}/omf/gramps
 
%post
if which scrollkeeper-update>/dev/null 2>&1; then scrollkeeper-update; fi

%postun
if which scrollkeeper-update>/dev/null 2>&1; then scrollkeeper-update; fi

%changelog
* Fri Jun 14 2002 Donald Peterson <dpeterso@engr.ors.edu>
- add scrollkeeper dependencies and some file cleanup
