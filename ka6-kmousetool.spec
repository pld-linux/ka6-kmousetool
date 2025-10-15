#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.08.2
%define		kframever	6.3.0
%define		qtver		6.7.0
%define		kaname		kmousetool
Summary:	kmousetool
Name:		ka6-%{kaname}
Version:	25.08.2
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ee7da81f5f26658aefd728d49f042866
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Multimedia-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-tools
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kstatusnotifieritem-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	phonon-qt6-devel
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMouseTool is a Linux-based KDE program. It clicks the mouse for you,
so you don't have to. KMouseTool works with any mouse or pointing
device.

%description -l pl.UTF-8
KMouseTool jest opartym na Linuksie programem KDE. Klika myszą za
Ciebie, więc Ty już nie musisz. KMouseTool działa z każdą myszą lub
innym urządzeniem wskazującym.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmousetool
%{_desktopdir}/org.kde.kmousetool.desktop
%{_iconsdir}/hicolor/*x*/actions/*.png
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_datadir}/kmousetool
%{_datadir}/metainfo/org.kde.kmousetool.appdata.xml
%lang(ca) %{_mandir}/ca/man1/kmousetool.1.*
%lang(de) %{_mandir}/de/man1/kmousetool.1.*
%lang(es) %{_mandir}/es/man1/kmousetool.1.*
%lang(et) %{_mandir}/et/man1/kmousetool.1.*
%lang(fr) %{_mandir}/fr/man1/kmousetool.1.*
%lang(it) %{_mandir}/it/man1/kmousetool.1.*
%lang(C) %{_mandir}/man1/kmousetool.1.*
%lang(nl) %{_mandir}/nl/man1/kmousetool.1.*
%lang(pt) %{_mandir}/pt/man1/kmousetool.1.*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kmousetool.1.*
%lang(sl) %{_mandir}/sl/man1/kmousetool.1*
%lang(sv) %{_mandir}/sv/man1/kmousetool.1.*
%lang(uk) %{_mandir}/uk/man1/kmousetool.1.*
