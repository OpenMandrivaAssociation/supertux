Summary:	Classic 2D jump n run sidescroller with Tux
Name:		supertux
Version:	0.4.0
Release:	2
License:	GPLv2+
Group:		Games/Arcade
Url:		http://supertux.berlios.de/
Source0:	https://github.com/SuperTux/supertux/releases/download/v%{version}/supertux-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
%if %mdvver >= 201500
Patch0:		supertux-0.4.0-use-system-squirrel.patch
%endif
Patch1:		supertux-0.4.0-tinygettext-subproject.patch
Patch2:		supertux-0.4.0-tinygettext-subproject-install.patch
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	physfs-devel
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_mixer)
%if %mdvver >= 201500
BuildRequires:	pkgconfig(squirrel)
%endif
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(zlib)

%description
SuperTux is a classic 2D jump 'n run sidescroller game in
a similar style like the original SuperMario games.

%files
%defattr(644,root,root,755)
%doc LICENSE.txt INSTALL.md README.md NEWS.md
%{_gamesdatadir}/%{name}2
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}*.png
%{_miconsdir}/%{name}*.png
%{_datadir}/applications/%{name}2.desktop
%{_datadir}/appdata/supertux2.appdata.xml
%{_datadir}/pixmaps/supertux.png
%attr(755,root,root) %{_gamesbindir}/%{name}2

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake \
	-DBUILD_SHARED_LIBS=OFF

%make

%install
%makeinstall_std -C build

rm -fr %{buildroot}%{_gamesdatadir}/doc/%{name}2-%{version}
rm -fr %{buildroot}%{_docdir}/supertux2

%if %mdvver < 201500
rm -f %{buildroot}%{_libdir}/libsquirrel.a
%endif

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

