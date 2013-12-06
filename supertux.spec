%define vname	%{name}2

Summary:	Classic 2D jump n run sidescroller with Tux
Name:		supertux
Version:	0.3.3
Release:	10
License:	GPLv2+
Group:		Games/Arcade
Url:		http://supertux.berlios.de/
Source0:	http://download.berlios.de/supertux/%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		supertux-0.3.3-use-system-squirrel.patch
Patch1:		supertux-0.3.3-gcc46.patch
Patch2:		supertux-0.3.3-ctypes.patch
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	physfs-devel
BuildRequires:	squirrel-devel
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(zlib)

%description
SuperTux is a classic 2D jump 'n run sidescroller game in
a similar style like the original SuperMario games. 

%prep
%setup -q
%apply_patches

%build
%cmake
%make 

%install
%makeinstall_std -C build
# (blino) required data files not automatically installed by 0.3.1
# install -m644 data/camera.cfg data/credits.txt %{buildroot}%{_gamesdatadir}/%{vname}

# mv %{buildroot}%{_gamesdatadir}/applications %{buildroot}%{_datadir}/
# mv %{buildroot}%{_gamesdatadir}/pixmaps %{buildroot}%{_datadir}/
rm -fr %{buildroot}%{_gamesdatadir}/doc/%{vname}-%{version}

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%files
%doc COPYING INSTALL README WHATSNEW.txt
%{_gamesdatadir}/%{vname}
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}*.png
%{_miconsdir}/%{name}*.png
%{_datadir}/applications/%{vname}.desktop
%{_datadir}/pixmaps/supertux.png
%{_gamesbindir}/%{vname}
%{_docdir}/supertux2/COPYING
%{_docdir}/supertux2/INSTALL
%{_docdir}/supertux2/README
%{_docdir}/supertux2/WHATSNEW.txt

