%bcond_without system_squirrel

Summary:	Classic 2D jump n run sidescroller with Tux
Name:		supertux
Version:	0.7.0
Release:	1
License:	GPLv2+
Group:		Games/Arcade
Url:		https://supertux.github.io/
Source0:	https://github.com/SuperTux/supertux/releases/download/v%{version}/SuperTux-v%{version}-Source.tar.gz
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		supertux-0.6.3-fix-libcurl-detection.patch
Patch1:		supertux-0.6.3-fix-data-search-path.patch
Patch3:		supertux-gcc12.patch
%if %{with system_squirrel}
Patch10:	supertux-0.6.3-use-system-squirrel.patch
BuildRequires:	pkgconfig(squirrel)
%endif
BuildSystem:	cmake
BuildOption:	-DIS_SUPERTUX_RELEASE:BOOL=ON
BuildOption:	-DBUILD_SHARED_LIBS:BOOL=OFF
BuildOption:	-DENABLE_BOOST_STATIC_LIBS:BOOL=OFF
BuildRequires:	boost-devel
BuildRequires:	git
BuildRequires:	physfs-devel
BuildRequires:	pkgconfig(glm)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libssh2)
BuildRequires:	pkgconfig(libidn2)
BuildRequires:	doxygen
BuildRequires:	ninja

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
%{_datadir}/pixmaps/supertux.png
%{_datadir}/icons/hicolor/scalable/apps/supertux2.svg
%{_datadir}/metainfo/supertux2.appdata.xml
%attr(755,root,root) %{_gamesbindir}/%{name}2

#----------------------------------------------------------------------------

%prep -a
%if %{with system_squirrel}
# Adapt to API changes in squirrel 3.2
sed -i -E 's|(sq_getinstanceup\(.*nullptr)(.*)|\1, false\2|g' src/scripting/wrapper.cpp
%endif
# try fix for boost 1.89
sed -i -e 's/\<system\>//' -e 's/  */ /g' CMakeLists.txt

%install -a
rm -fr %{buildroot}%{_gamesdatadir}/doc/%{name}2-%{version}
rm -fr %{buildroot}%{_docdir}/supertux2

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png
