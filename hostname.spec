Summary: Utility to set/show the host name or domain name
Name: hostname
Version: 3.13
Release: 1%{?dist}
License: GPLv2+
Group: System Environment/Base
URL: http://packages.qa.debian.org/h/hostname.html
Source0: http://ftp.de.debian.org/debian/pool/main/h/hostname/hostname_%{version}.tar.gz

# Initial changes
Patch1: hostname-rh.patch

%description
This package provides commands which can be used to display the system's
DNS name, and to display or set its hostname or NIS domain name.

%prep
%setup -q
%patch1 -p1 -b .rh

%build
make CFLAGS="$RPM_OPT_FLAGS $CFLAGS"

%install
make BASEDIR=%{buildroot} install

%files
%doc COPYRIGHT
/bin/*
%{_mandir}/man1/*

%changelog
* Tue Jun 18 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13-1
- 3.13: -v references removed upstream

* Tue Mar 26 2013 Jiri Popelka <jpopelka@redhat.com> - 3.12-4
- remove void -v option from --help

* Fri Mar 08 2013 Jiri Popelka <jpopelka@redhat.com> - 3.12-3
- do not ship outdated french man pages (#919198)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 07 2012  Jiri Popelka <jpopelka@redhat.com> - 3.12-1
- 3.12: man page improvements

* Fri Nov 30 2012  Jiri Popelka <jpopelka@redhat.com> - 3.11-4
- revert /usr move for now

* Fri Nov 30 2012  Jiri Popelka <jpopelka@redhat.com> - 3.11-3
- remove some rh-specific bits from rh.patch as they are no longer valid (#881913)
- remove outdated de & pt man pages
- /usr move: use _bindir macro

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 21 2012  Jiri Popelka <jpopelka@redhat.com> - 3.11-1
- 3.11

* Wed Jan 18 2012  Jiri Popelka <jpopelka@redhat.com> - 3.10-1
- 3.10

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 29 2011  Jiri Popelka <jpopelka@redhat.com> - 3.09-1
- 3.09

* Sat Dec 24 2011  Jiri Popelka <jpopelka@redhat.com> - 3.08-1
- 3.08

* Fri Dec 23 2011  Jiri Popelka <jpopelka@redhat.com> - 3.07-1
- 3.07

* Mon Mar 07 2011  Jiri Popelka <jpopelka@redhat.com> - 3.06-1
- 3.06

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010  Jiri Popelka <jpopelka@redhat.com> - 3.05-1
- 3.05

* Fri Apr 30 2010 Ville Skyttä <ville.skytta@iki.fi> - 3.04-2
- Mark localized man pages with %%lang.

* Thu Mar 25 2010  Jiri Popelka <jpopelka@redhat.com> - 3.04-1
- 3.04

* Tue Feb 02 2010  Jiri Popelka <jpopelka@redhat.com> - 3.03-1
- 3.03

* Tue Nov 10 2009  Jiri Popelka <jpopelka@redhat.com> - 3.01-1
- Initial package. Up to now hostname has been part of net-tools package.
- This package is based on Debian's hostname because Debian has had hostname
  as separate package since 1997 and the code is much better then the old one
  contained in net-tools.
