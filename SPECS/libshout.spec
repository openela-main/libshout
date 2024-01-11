Name:           libshout
Version:        2.2.2
Release:        19%{?dist}
Summary:        Icecast source streaming library

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.icecast.org/
Source:         http://downloads.us.xiph.org/releases/libshout/libshout-%{version}.tar.gz
Patch0:         libshout-2.2.2-fix_speex.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libtheora-devel
BuildRequires:  speex-devel



%description
libshout is a library for communicating with and sending data to an
icecast server.  It handles the socket connection, the timing of the
data, and prevents most bad data from getting to the icecast server.

%package        devel
Summary:        static libraries and header files for %{name} development.
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

Requires:       libogg-devel
Requires:       libvorbis-devel
Requires:       libtheora-devel
Requires:       speex-devel

%description    devel
The libshout-devel package contains the header files needed for developing
applications that send data to an icecast server.  Install libshout-devel if
you want to develop applications using libshout.

%prep
%setup -q
%patch0 -p1 -b .fix_speex

%build
%configure --disable-static

# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR="$RPM_BUILD_ROOT" INSTALL="install -p " install

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING NEWS README
%{_libdir}/libshout.so.*

%files devel
%defattr(-,root,root,-)
%doc examples/*.c doc/*.xml doc/*.xsl
%{_libdir}/libshout.so
%{_libdir}/pkgconfig/shout.pc
%dir %{_includedir}/shout/
%{_includedir}/shout/shout.h
%{_datadir}/aclocal/shout.m4

%changelog
* Fri Jul 27 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2.2-19
- Dropped unused libshout.autotools patch

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.2-3
- Autorebuild for GCC 4.3

* Fri Dec  7 2007 kwizart < kwizart at gmail.com > - 2.2.2-2
- Fix http://bugzilla.redhat.com/415121
- Add disable-static
- Don't use makeinstall macro
- Update License field

* Thu Sep 07 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.2.2-1
- updated to new release

* Fri Mar 17 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.2-3
- add Requires: to -devel package

* Fri Mar 17 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.2-2
- rebuild to please the extras repository

* Fri Mar 10 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.2-1
- new (incompatible) version, but deps are updated
- various cleanups

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.0.9-4
- rebuild on all arches

* Fri Apr  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.9-3
- Include headers directory entry in -devel package.

* Sat Feb 26 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.0.9-2
- Remove redundant explicit /sbin/ldconfig dependency.

* Wed Jun 04 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.9-0.fdr.1: initial RPM release
