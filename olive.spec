#For git snapshots, set to 0 to use release instead:
%global usesnapshot 1
%if 0%{?usesnapshot}
# https://github.com/olive-editor/olive/commit/5fce683e0d78c8db7dbd1604fab6a1899c085571
%global commit0 5fce683e0d78c8db7dbd1604fab6a1899c085571
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20221118
%endif
%global unique_name org.olivevideoeditor.Olive
%global appl_name application-vnd.olive-project

%undefine __cmake_in_source_build

Name:           olive
Version:        0.2.0
%if 0%{?usesnapshot}
Release:        0.15.%{gitdate}git%{shortcommit0}%{?dist}
%else
Release:        20%{?dist}
%endif
Summary:        A free non-linear video editor
License:        GPLv3+
Url:            https://www.olivevideoeditor.org
%if 0%{?usesnapshot}
Source0:        https://github.com/olive-editor/%{name}/archive/%{commit0}/%{name}-%{gitdate}git%{shortcommit0}.tar.gz
%else
Source0:        https://github.com/olive-editor/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif
Patch0:         armv7_build_fix.patch

BuildRequires:  cmake
BuildRequires:  frei0r-devel
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qttranslations
BuildRequires:  OpenColorIO-devel
BuildRequires:  OpenImageIO-devel
BuildRequires:  ilmbase-devel
BuildRequires:  portaudio-devel
Requires:       hicolor-icon-theme

# ext/sse2neon.h:106:2: error: #error "You must enable NEON instructions (e.g. -mfpu=neon) to use SSE2NEON."
ExcludeArch: armv7hl

%description
%{name} is a free non-linear video editor aiming to provide a fully-featured
alternative to high-end professional video editing software.

%{name} is in Alpha stage, so expect bugs/crashes and feel free to report them.
Builds for Linux, Mac, and Windows are available.

At the moment, most of the information here is for v0.1.0 (git hash 1e3cf53), as
%{name} is currently undergoing a major overhaul, including a new "node editing"
system. The wiki will contain new info once it is finalized, so stay tuned.

A Feature list is a the moment not available.

%prep
%if 0%{?usesnapshot}
%autosetup -p1 -n %{name}-%{commit0}
%else
%autosetup -p1 -n %{name}-%{version}
%endif

# Override the pathetic ffmpeg test
sed -i -e 's@3.0@@g' CMakeLists.txt

%build
%cmake -DUSE_WERROR=OFF
%cmake_build

%install
%cmake_install
rm -rf %buildroot/usr/share/icons/hicolor/1024x1024

#%%find_lang %%{name} --all-name --with-qt
find %{buildroot}%{_datadir}/%{name}-editor/ts -name "*.qm" | sed 's:'%{buildroot}'::
s:.*/\([a-zA-Z]\{2\}\).qm:%lang(\1) \0:' > %{name}.lang

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{unique_name}.appdata.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}-editor
%{_datadir}/applications/%{unique_name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{unique_name}.png
%{_datadir}/icons/hicolor/*/mimetypes/%{appl_name}.png
%{_metainfodir}/%{unique_name}.appdata.xml
%{_datadir}/mime/packages/%{unique_name}.xml
#%%{_datadir}/%%{name}-editor/effects
#%%{_datadir}/%%{name}-editor

%changelog
* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.0-0.15.20221118git5fce683
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.0-0.14.20221118git5fce683
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.0-0.13.20221118git5fce683
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Leigh Scott <leigh123linux@gmail.com> - 0.2.0-0.12.20221118git5fce683
- Rebuild for new ffmpeg

* Wed Feb 08 2023 Leigh Scott <leigh123linux@gmail.com> - 0.2.0-0.11.20221118git5fce683
- rebuilt

* Sat Nov 19 2022 Sérgio Basto <sergio@serjux.com> - 0.2.0-0.10.20221118git5fce683
- Update to olive-20221118git5fce683
- add armv7_build_fix.patch

* Fri Nov 11 2022 Leigh Scott <leigh123linux@gmail.com> - 0.1.2-0.9.20220818gitb169ad9
- rebuilt

* Mon Aug 22 2022 Sérgio Basto <sergio@serjux.com> - 0.1.2-0.8.20220818gitb169ad9
- Update snapshot to 20220818

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.2-0.7.20220228git41a49c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Mar 03 2022 Nicolas Chauvet <kwizart@gmail.com> - 0.1.2-0.6.20220228git41a49c4
- Rebuilt

* Wed Mar 02 2022 Sérgio Basto <sergio@serjux.com> - 0.1.2-0.5.20220228git41a49c4
- New snapshot, ffmpeg 5 compatible

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Leigh Scott <leigh123linux@gmail.com> - 0.1.2-5
- Rebuilt for new ffmpeg snapshot
- Add olive-0.1.2-qt5.15.patch

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.2-3
- Rebuild for ffmpeg-4.3 git

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2-1

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 0.1.0-0.4.20190515git55c5b00
- Rebuild for new ffmpeg version

* Fri May 17 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-0.3.20190515git55c5b00
- Add a more meaningful description and summary

* Thu May 16 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-0.2.20190515git55c5b00
- Update to 0.1.0-0.2.20190515git55c5b00
- Switch Build to cmake
- Remove BR hicolor-icon-theme
- Use %%autsetup
- Add BR pkgconfig(Qt5Svg)
- Add BR cmake3
- Use %%cmake3 macro instead of %%cmake
- Use %%{_metainfodir} macro

* Fri May 03 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-0.1.20190503git99b6ba6
- Update to 0.1.0-0.1.20190503git99b6ba6

* Wed Feb 06 2019 Martin Gansser <martinkg@fedoraproject.org> - 0-0.1.20190206gitfc96ad7
- initial package, not even released as version 0.1...
