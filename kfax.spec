Summary:	A fax viewing program
Name:		kfax
Version: 	3.3.6
Release: 	8
Source0: 	http://fr2.rpmfind.net/linux/KDE/stable/4.0.4/src/extragear/%name-%version-kde4.3.1.tar.bz2
Patch0:		kfax-3.3.6-kde4.3.1-x11.patch
License: 	GPLv2+
Group: 		Graphics
Url: 		http://www.kde.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel
%if %mdkversion >= 200910
Obsoletes:	kdegraphics-kfax < 1:3.5.10-3
%endif
%if %mdkversion >= 200100
Obsoletes:  kdegraphics3-kfax < 1:3.5.10-5
%endif
Conflicts:	kde-l10n < 3.5.9-5

%description 
A program to display raw and tiffed fax images (g3, g3-2d, g4).

%files -f %name.lang
%doc COPYING ChangeLog README
%_kde_bindir/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/%name
%_kde_iconsdir/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version-kde4.3.1
%patch0 -p1

%build

%cmake_kde4
%make

%install
cd build
%{makeinstall_std}
cd -

%find_lang %name --with-html


