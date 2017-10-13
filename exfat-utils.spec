Name:		exfat-utils
Summary:	Utilities for exFAT file system
Version:	1.2.7
Release:	1%{?dist}
License:	GPLv2+
Group:		System Environment/Base
Source0:	https://github.com/relan/exfat/releases/download/v%{version}/exfat-utils-%{version}.tar.gz
URL:		https://github.com/relan/exfat

%description
A set of utilities for creating, checking, dumping and labeling exFAT file
system.

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p %{buildroot}/%{_mandir}/man8/
cp -a dump/dumpexfat.8 %{buildroot}/%{_mandir}/man8/dumpexfat.8
cp -a fsck/exfatfsck.8 %{buildroot}/%{_mandir}/man8/exfatfsck.8
ln -s %{_mandir}/man8/exfatfsck.8 %{buildroot}/%{_mandir}/man8/fsck.exfat.8
cp -a mkfs/mkexfatfs.8 %{buildroot}/%{_mandir}/man8/mkexfatfs.8
ln -s %{_mandir}/man8/mkexfatfs.8 %{buildroot}/usr/share/man/man8/mkfs.exfat.8
cp -a label/exfatlabel.8 %{buildroot}/%{_mandir}/man8/exfatlabel.8


%files
%doc COPYING
%{_sbindir}/dumpexfat
%{_sbindir}/exfatfsck
%{_sbindir}/fsck.exfat
%{_sbindir}/mkexfatfs
%{_sbindir}/mkfs.exfat
%{_sbindir}/exfatlabel
%{_mandir}/man8/*

%changelog

* Fri Oct 13 2017 David Va <davidva AT tutanota DOT com> - 1.2.7-1
- Updated to 1.2.7

* Wed Mar 30 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-1
- Update to 1.2.3

* Sat Nov 14 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Sat Dec 20 2014 TingPing <tingping@tingping.se> - 1.1.1-1
- Update to 1.1.1

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 17 2013 TingPing <tingping@tingping.se> - 1.0.1-1
- Initial package

