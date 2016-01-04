#
# Spec file for package qownnotes
#
# Check for Linux distribution version numbers here:
# https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
#


Name:           qownnotes
BuildRequires:  gcc gcc-c++ fdupes

%if 0%{?suse_version}
%endif

# This is for all Fedora and CentOS 7
%if 0%{?fedora} || 0%{?centos_version} == 700 || 0%{?rhel_version} == 700

BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-gui
#BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qttools qt5-qttools-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  desktop-file-utils
Requires:       qt5-qtsvg

%else
# This is for all SUSE

BuildRequires:  libqt5-qtbase-devel libQt5Script-devel libQt5Svg-devel
BuildRequires:  update-desktop-files 
Requires:       libQt5Svg5

%endif

License:        GPL-2.0
Group:          System/GUI/Productivity
Summary:        A note-taking app and todo list manager that can synchronize with your owncloud notes
Url:            http://www.qownnotes.org/
Version:        VERSION-STRING
Release:        1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.xz


%description
QOwnNotes is the open source notepad and todo list manager, that works together with the default notes application of ownCloud.

So you are able to write down your thoughts with QOwnNotes and edit or search for them later from your mobile device (like with CloudNotes or the ownCloud web-service.

The notes are stored as plain text files and are synced with ownCloud's file sync functionality. Of course other software, like Dropbox can be used too.

I like the concept of having notes accessible in plain text files, like it is done in the ownCloud notes app, to gain a maximum of freedom, but I was not able to find a decent desktop note taking tool or a text editor, that handles them well. Out of this need QOwnNotes was born.

www.qownnotes.org

Author
======
Patrizio Bekerle <patrizio@bekerle.com>


%prep
%setup -q 
mkdir build
pushd build
qmake-qt5 ../src
popd

%build
echo centos_version 0%{?centos_version}
echo rhel_version   0%{?rhel_version}
echo fedora 0%{?fedora}
echo suse_version   0%{?suse_version}

pushd build
CFLAGS=$RPM_OPT_FLAGS CCFLAGS=$CFLAGS

%if 0%{?fedora}

make

%else

%make_jobs

%endif

popd

%install
pushd build
install -D -m 0755 QOwnNotes $RPM_BUILD_ROOT/%{_prefix}/bin/QOwnNotes
popd
install -D -m 0644 src/images/icons/128x128/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/QOwnNotes.png
install -D -m 0644 src/images/icons/16x16/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/16x16/apps/QOwnNotes.png
install -D -m 0644 src/images/icons/24x24/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/24x24/apps/QOwnNotes.png
install -D -m 0644 src/images/icons/32x32/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/QOwnNotes.png
install -D -m 0644 src/images/icons/48x48/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/QOwnNotes.png
install -D -m 0644 src/images/icons/64x64/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/64x64/apps/QOwnNotes.png
install -D -m 0644 src/images/icons/96x96/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/96x96/apps/QOwnNotes.png
install -D -m 0644 src/images/icons/128x128/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/128x128/apps/QOwnNotes.png
install -D -m 0644 src/images/icons/256x256/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/QOwnNotes.png
install -D -m 0644 src/images/icons/512x512/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/512x512/apps/QOwnNotes.png

%if 0%{?suse_version}
%suse_update_desktop_file -c  QOwnNotes QOwnNotes QOwnNotes QOwnNotes QOwnNotes "Utility;SyncUtility;"
%endif

%fdupes $RPM_BUILD_ROOT/%{_prefix}

%clean  
rm -rf $RPM_BUILD_ROOT  

%files
%defattr(-,root,root)
%doc LICENSE README.md CHANGELOG.md SHORTCUTS.md
%{_bindir}/QOwnNotes
%{_datadir}/pixmaps/QOwnNotes.png

%{_datadir}/icons/hicolor/16x16/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/24x24/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/32x32/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/48x48/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/64x64/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/96x96/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/128x128/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/256x256/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/512x512/apps/QOwnNotes.png
%{_datadir}/applications/QOwnNotes.desktop

%dir %{_datadir}/icons/hicolor/512x512/apps
%dir %{_datadir}/icons/hicolor/256x256/apps
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/96x96/apps
%dir %{_datadir}/icons/hicolor/64x64/apps
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/32x32/apps
%dir %{_datadir}/icons/hicolor/24x24/apps
%dir %{_datadir}/icons/hicolor/16x16/apps
%dir %{_datadir}/icons/hicolor/512x512
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/96x96
%dir %{_datadir}/icons/hicolor/64x64
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/24x24
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor

%changelog



