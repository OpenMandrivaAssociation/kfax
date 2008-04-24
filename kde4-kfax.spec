%define version 4.0
%define release %mkrel 0.beta5.1
%define oname   kfax-kde4

Name:		kde4-kfax
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Url:		http://www.kde.org/
Group:		Graphical desktop/KDE
Source0:	%{oname}-beta5.tar.bz2
Summary:        kfaxis  a program to display raw and tiffed fax images (g3, g3-2d, g4)
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  cmake >= 2.4.5
BuildRequires:  kdelibs4-devel


%description
KFax is  a program to display raw and tiffed fax images (g3, g3-2d, g4)

%post
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_desktop_database}
%clean_icon_cache hicolor

%files
%defattr(-,root,root)
%{_kde_bindir}/kfax
%{_kde_datadir}/applications/kde4/kfax.desktop
%dir %{_kde_appsdir}/kfax
%{_kde_appsdir}/kfax/kfaxui.rc
%dir %{_kde_appsdir}/kfax/pics
%{_kde_appsdir}/kfax/pics/kfax.tif
%{_kde_appsdir}/kfax/pics/kfaxlogo.xpm
%{_kde_iconsdir}/*/*/*/kfax.*
%{_kde_datadir}/locale/*/LC_SCRIPTS/*/*


#------------------------------------------------

%prep
%setup -q -n %oname-beta5

%build
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}


%clean
rm -rf %buildroot
