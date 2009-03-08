%define name	supertux
%define vname	%{name}2
%define version 0.3.1
%define rel	2
%define release	%mkrel %rel
%define Summary Classic 2D jump 'n run sidescroller with Tux

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://download.berlios.de/supertux/%{name}-%{version}c.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		supertux-0.3.1-fix-menu-path.patch
Patch1:		supertux-0.3.1-gcc43.patch
Patch2:     supertux-0.3.1-fix-format-string.patch
License:	GPLv2+
Group:		Games/Arcade
URL:		http://supertux.berlios.de/
Summary:	%{Summary}
BuildRequires:	jam
BuildRequires:	SDL_mixer-devel SDL_image-devel MesaGLU-devel
BuildRequires:	oggvorbis-devel openal-devel physfs-devel zlib-devel 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SuperTux is a classic 2D jump 'n run sidescroller game in
a similar style like the original SuperMario games. 

%prep
%setup -q
%patch0 -p1 -b .path
%patch1 -p1 -b .gcc43
%patch2 -p0

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--disable-debug
jam

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=%{buildroot} jam install
# (blino) required data files not automatically installed by 0.3.1
install -m644 data/camera.cfg data/credits.txt %{buildroot}%{_gamesdatadir}/%{vname}

mv %{buildroot}%{_gamesdatadir}/applications %{buildroot}%{_datadir}/
mv %{buildroot}%{_gamesdatadir}/pixmaps %{buildroot}%{_datadir}/
rm -fr %{buildroot}%{_gamesdatadir}/doc/%{vname}-%{version}

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README WHATSNEW.txt
%{_gamesdatadir}/%{vname}
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}*.png
%{_miconsdir}/%{name}*.png
%{_datadir}/applications/%{vname}.desktop
%{_datadir}/pixmaps/supertux.png
%defattr(755,root,root,755)
%{_gamesbindir}/%{vname}
