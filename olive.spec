# https://github.com/olive-editor/olive/commit/55c5b004875bec0e0b73789df561eef9d1395ebd
%global commit0 55c5b004875bec0e0b73789df561eef9d1395ebd
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20190515
%global unique_name org.olivevideoeditor.Olive
%global appl_name application-vnd.olive-project

Name:           olive
Version:        0.1.0
Release:        0.4.%{gitdate}git%{shortcommit0}%{?dist}
Summary:        A free non-linear video editor
License:        GPLv3+
Url:            https://www.olivevideoeditor.org
Source0:        https://github.com/olive-editor/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  cmake3
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
Requires:       hicolor-icon-theme

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
%autosetup -n %{name}-%{commit0}

%build
%cmake3 .
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
rm -rf %buildroot/usr/share/icons/hicolor/1024x1024

%find_lang %{name} --all-name --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{unique_name}.appdata.xml

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}-editor
%{_datadir}/applications/%{unique_name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{unique_name}.png
%{_datadir}/icons/hicolor/*/mimetypes/%{appl_name}.png
%{_metainfodir}/%{unique_name}.appdata.xml
%{_datadir}/mime/packages/%{unique_name}.xml
%{_datadir}/%{name}-editor

%changelog
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
