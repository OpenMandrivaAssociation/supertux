%define name	supertux
%define vname	%{name}2
%define version 0.3.3
%define release	%mkrel 6
%define Summary Classic 2D jump n run sidescroller with Tux

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://download.berlios.de/supertux/%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		supertux-0.3.3-use-system-squirrel.patch
Patch1:		supertux-0.3.3-gcc46.patch
Patch2:		supertux-0.3.3-ctypes.patch
License:	GPLv2+
Group:		Games/Arcade
URL:		http://supertux.berlios.de/
Summary:	%{Summary}
BuildRequires:	cmake
BuildRequires:	libcurl-devel
BuildRequires:	SDL_mixer-devel SDL_image-devel mesaglu-devel libglew-devel
BuildRequires:	oggvorbis-devel openal-devel physfs-devel zlib-devel boost-devel
BuildRequires:	libsquirrel-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build
# (blino) required data files not automatically installed by 0.3.1
# install -m644 data/camera.cfg data/credits.txt %{buildroot}%{_gamesdatadir}/%{vname}

# mv %{buildroot}%{_gamesdatadir}/applications %{buildroot}%{_datadir}/
# mv %{buildroot}%{_gamesdatadir}/pixmaps %{buildroot}%{_datadir}/
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
%doc COPYING INSTALL README WHATSNEW.txt
%{_gamesdatadir}/%{vname}
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}*.png
%{_miconsdir}/%{name}*.png
%{_datadir}/applications/%{vname}.desktop
%{_datadir}/pixmaps/supertux.png
%defattr(755,root,root,755)
%{_gamesbindir}/%{vname}
%{_docdir}/supertux2/COPYING
%{_docdir}/supertux2/INSTALL
%{_docdir}/supertux2/README
%{_docdir}/supertux2/WHATSNEW.txt


%changelog
* Wed Mar 28 2012 Andrew Lukoshko <andrew.lukoshko@rosalab.ru> 0.3.3-6
- fixed build with recent curl
- update BR

* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 0.3.3-5mdv2011.0
+ Revision: 670630
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.3-4mdv2011.0
+ Revision: 607757
- rebuild

  + Götz Waschk <waschk@mandriva.org>
    - replace patch and kludge by a clean patch (anaselli)

* Tue Mar 23 2010 Götz Waschk <waschk@mandriva.org> 0.3.3-3mdv2010.1
+ Revision: 526769
- build with system squirrel

* Tue Mar 23 2010 Zombie Ryushu <ryushu@mandriva.org> 0.3.3-2mdv2010.1
+ Revision: 526715
- Change to use cmake macro
- Change to use cmake macro
- Change to use cmake macro
- Change to use cmake macro

* Tue Mar 23 2010 Zombie Ryushu <ryushu@mandriva.org> 0.3.3-1mdv2010.1
+ Revision: 526702
- Fix libglew dependency
- Fix Boost dependency
- Upgrade to 0.3.3
- Upgrade to 0.3.3

* Mon Jan 04 2010 Götz Waschk <waschk@mandriva.org> 0.3.1-5mdv2010.1
+ Revision: 486251
- enable libcurl support

* Sun Oct 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-4mdv2010.0
+ Revision: 453717
- rebuild for new libopenal

* Fri May 22 2009 Rémy Clouard <shikamaru@mandriva.org> 0.3.1-3mdv2010.0
+ Revision: 378774
- fix missing include

* Sun Mar 08 2009 Michael Scherer <misc@mandriva.org> 0.3.1-2mdv2009.1
+ Revision: 352727
- add patch2, fix format string error

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Tue Aug 26 2008 Funda Wang <fwang@mandriva.org> 0.3.1-1mdv2009.0
+ Revision: 276388
- add gcc 4.3 patch from fedora

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 04 2008 Olivier Blin <oblin@mandriva.com> 0.3.1-1mdv2008.1
+ Revision: 144886
- install missing data files
- 0.3.1
- rediff menu patch
- restore buildroot

* Sun Dec 23 2007 Funda Wang <fwang@mandriva.org> 0.3.0-3mdv2008.1
+ Revision: 137297
- remove wrong doc files
- drop dependency on d-f-i
- fix desktop entry icon
- drop old menu

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Apr 24 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.0-2mdv2008.0
+ Revision: 17922
- fix path to binary in menu (P0, fixes #30430)


* Thu Dec 28 2006 Olivier Blin <oblin@mandriva.com> 0.3.0-1mdv2007.0
+ Revision: 102381
- BuildRequires openal-devel
- buildrequires oggvorbis-devel
- buildrequire physfs-devel
- 0.3.0

* Thu Nov 02 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.1.3-5mdv2007.1
+ Revision: 75959
- add BuildRequires: desktop-file-utils
- Import supertux

* Fri Jul 14 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.1.3-4mdv2007.0
- XDG
- Add patch 0 : Fix Build

* Mon May 08 2006 Stefan van der Eijk <stefan@eijk.nu> 0.1.3-3mdk
- rebuild for sparc

* Tue Jul 12 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.1.3-2mdk
- fix desktopdir & icondir

* Mon Jul 11 2005 Eskild Hustvedt <eskild@mandriva.org> 0.1.3-1mdk
- New version 0.1.3
- %%mkrel

* Thu Jan 27 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.2-2mdk
- update summary and description

* Fri Aug 27 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.2-1mdk
- 1.1.2

* Wed Jun 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.1-2mdk
- rebuild

* Thu May 13 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.1-1mdk
- 0.1.1

* Fri May 07 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.1.0-1mdk
- New release 0.1.0

* Sun May 02 2004 Marcel Pol <mpol@mandrake.org> 0.0.6-3mdk
- new url

* Sun May 02 2004 Marcel Pol <mpol@mandrake.org> 0.0.6-2mdk
- buildrequires

* Fri Apr 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.0.6-1mdk
- 0.0.6
- drop P0

