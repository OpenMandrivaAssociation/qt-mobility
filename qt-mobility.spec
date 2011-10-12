# Build examples
%bcond_without examples
# Build demos
%bcond_without demos

%define major 1

%define snap 20110922

%define libnamedev %mklibname %{name} -d
%define libqtbearer %mklibname qtbearer %major
%define libqtcontacts %mklibname qtcontacts %major
%define libqtconnectivity %mklibname qtconnectivity %major
%define libqtfeedback %mklibname qtfeedback %major
%define libqtgallery %mklibname qtgallery %major
%define libqtlocation %mklibname qtlocation %major
%define libqtmultimediakit %mklibname qtmultimediakit %major
%define libqtorganizer %mklibname qtorganizer %major
%define libqtpublishsubscribe %mklibname qtpublishsubscribe %major
%define libqtsensors %mklibname qtsensors %major
%define libqtserviceframework %mklibname qtserviceframework %major
%define libqtsysteminfo %mklibname qtsysteminfo %major
%define libqtversit %mklibname qtversit %major
%define libqtversitorganizer %mklibname qtversitorganizer %major

%define _qt4_datadir		%{_prefix}/lib/qt4
%define _qt4_bindir		%{_qt4_datadir}/bin
%define _qt4_docdir		%{_docdir}/qt4
%define _qt4_libdir		%{_libdir}
%define _qt4_includedir		%{_qt4_datadir}/include
%define _qt4_plugindir		%{_libdir}/qt4/plugins
%define _qt4_demodir		%{_qt4_datadir}/demos
%define _qt4_exampledir		%{_qt4_datadir}/examples
%define _qt4_importdir		%{_qt4_datadir}/imports
%define _qt4_translationdir	%{_qt4_datadir}/translations

Name:		qt-mobility
Summary:	Qt Mobility Framework
Group:		Development/Other
Version:	1.2.0
Release:	1
License:	LGPLv2 with exceptions
URL:		http://qt.nokia.com/products/qt-addons/mobility 
%if 0%{?snap:1}
# git clone git://gitorious.org/qt-mobility/qt-mobility.git
# cd qt-mobility; git archive --prefix=qt-mobility-opensource-src-1.2.0/ master | xz -9 >  qt-mobility-opensources-src-1.2.0-20110922.tar.xz
Source0: qt-mobility-opensource-src-1.2.0-%{snap}.tar.xz
%else
Source0: http://get.qt.nokia.com/qt/add-ons/qt-mobility-opensource-src-%{version}.tar.gz
%endif
Patch1:                qt-mobility-opensource-src-1.1.0-pulseaudio-lib.patch
## upstreamable patches
Patch50: qt-mobility-opensource-src-1.2.0-translationsdir.patch
BuildRequires:	alsa-lib-devel
BuildRequires:	bluez-devel
BuildRequires:	libblkid-devel
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	libxrandr-devel
BuildRequires:	libxv-devel
BuildRequires:	networkmanager-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	udev-devel
BuildRequires:	qt4-devel
BuildRequires:	gdb
# WARNING: still isnt possible to build against qmf
BuildConflicts:	qmf-devel
Provides:	qt4-mobility = %{version}-%{release}

%description
Qt Mobility Project delivers a set of new APIs to Qt with features that are well
known from the mobile device world, in particular phones. However, these APIs
allow the developer to use these features with ease from one framework and apply
them to phones, netbooks and non-mobile personal computers. The framework not
only improves many aspects of a mobile experience, because it improves the use
of these technologies, but has applicability beyond the mobile device arena.

%files
%doc LICENSE.LGPL LGPL_EXCEPTION.txt
%{_qt4_importdir}/QtMobility/
%{_qt4_importdir}/QtMultimediaKit/
%{_qt4_plugindir}/*

#--------------------------------------------------------------------

%package -n %{libqtbearer}

Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtbearer}
Qt Mobility Framework library.

%files -n %{libqtbearer}
%{_qt4_libdir}/libQtBearer.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libqtcontacts}

Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtcontacts}
Qt Mobility Framework library.

%files -n %{libqtcontacts}
%{_qt4_libdir}/libQtContacts.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libqtconnectivity}
Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtconnectivity}
Qt Mobility Framework library.

%files -n %{libqtconnectivity}
%{_qt4_libdir}/libQtConnectivity.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libqtfeedback}
Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtfeedback}
Qt Mobility Framework library.

%files -n %{libqtfeedback}
%{_qt4_libdir}/libQtFeedback.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libqtgallery}
Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtgallery}
Qt Mobility Framework library.

%files -n %{libqtgallery}
%{_qt4_libdir}/libQtGallery.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libqtlocation}
Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtlocation}
Qt Mobility Framework library.

%files -n %{libqtlocation}
%{_qt4_libdir}/libQtLocation.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libqtmultimediakit}
Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtmultimediakit}
Qt Mobility Framework library.

%files -n %{libqtmultimediakit}
%{_qt4_libdir}/libQtMultimediaKit.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libqtorganizer}
Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtorganizer}
Qt Mobility Framework library.

%files -n %{libqtorganizer}
%{_qt4_libdir}/libQtOrganizer.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libqtpublishsubscribe}
Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtpublishsubscribe}
Qt Mobility Framework library.

%files -n %{libqtpublishsubscribe}
%{_qt4_libdir}/libQtPublishSubscribe.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libqtsensors}
Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtsensors}
Qt Mobility Framework library.

%files -n %{libqtsensors}
%{_qt4_libdir}/libQtSensors.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libqtserviceframework}
Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtserviceframework}
Qt Mobility Framework library.

%files -n %{libqtserviceframework}
%{_qt4_libdir}/libQtServiceFramework.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libqtsysteminfo}
Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtsysteminfo}
Qt Mobility Framework library.

%files -n %{libqtsysteminfo}
%{_qt4_libdir}/libQtSystemInfo.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libqtversit}
Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtversit}
Qt Mobility Framework library.

%files -n %{libqtversit}
%{_qt4_libdir}/libQtVersit.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libqtversitorganizer}
Summary:	Qt Mobility Framework library
Group:		System/Libraries

%description -n %{libqtversitorganizer}
Qt Mobility Framework library.

%files -n %{libqtversitorganizer}
%{_qt4_libdir}/libQtVersitOrganizer.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libnamedev}
Summary:	Qt Mobility Framework development files
Group:		Development/KDE and Qt
Requires:	qt4-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	qt4-mobility-devel = %{version}-%{release}

Requires:  	%libqtbearer = %{version}-%{release}
Requires:       %libqtcontacts = %{version}-%{release}
Requires:       %libqtconnectivity = %{version}-%{release}
Requires:       %libqtfeedback = %{version}-%{release}
Requires:       %libqtgallery = %{version}-%{release}
Requires:       %libqtlocation = %{version}-%{release}
Requires:       %libqtmultimediakit = %{version}-%{release}
Requires:       %libqtorganizer = %{version}-%{release}
Requires:       %libqtpublishsubscribe = %{version}-%{release}
Requires:       %libqtsensors = %{version}-%{release}
Requires:       %libqtserviceframework = %{version}-%{release}
Requires:       %libqtsysteminfo = %{version}-%{release}
Requires:       %libqtversit = %{version}-%{release}
Requires:       %libqtversitorganizer = %{version}-%{release}

%description -n %{libnamedev}
Development files to build applications that use Qt Webkit.

%files -n %{libnamedev}
%defattr(-,root,root,-)
%{_qt4_bindir}/icheck
%{_qt4_bindir}/ndefhandlergen
%{_qt4_bindir}/qcrmlgen
%{_qt4_bindir}/servicedbgen
%{_qt4_bindir}/servicefw
%{_qt4_bindir}/servicexmlgen
%{_qt4_bindir}/vsexplorer
%{_qt4_datadir}/mkspecs/features/mobility.prf
%{_qt4_datadir}/mkspecs/features/mobilityconfig.prf 
%{_qt4_includedir}/Qt*/
%{_qt4_libdir}/libQt*.prl
%{_qt4_libdir}/libQt*.so

#--------------------------------------------------------------------

%package doc
Summary:	Qt Mobility API documentation
Group:		Books/Howtos
BuildArch:	noarch
Suggests:	qt4-doc
Provides:	qt4-mobility-doc = %{version}-%{release}

%description doc
API documentation files for Qt Mobility.

%files doc
%defattr(-,root,root,-)
%{_docdir}/html/qtmobility/

#--------------------------------------------------------------------

%if %{with examples}
%package examples
Summary:	Qt Mobility Framework examples
Group:		System/X11
Provides:	qt4-mobility-examples = %{version}-%{release}

%description examples
Example files for the Qt Mobility Framework.

%files examples
%defattr(-,root,root,-)
%{_qt4_bindir}/accel
%{_qt4_bindir}/annotatedurl
%{_qt4_bindir}/arrowkeys
%{_qt4_bindir}/audiodevices
%{_qt4_bindir}/audioinput
%{_qt4_bindir}/audiooutput
%{_qt4_bindir}/audiorecorder
%{_qt4_bindir}/battery-publisher
%{_qt4_bindir}/battery-subscriber/
%{_qt4_bindir}/bearercloud
%{_qt4_bindir}/bearermonitor
%{_qt4_bindir}/btchat
%{_qt4_bindir}/btfiletransfer
%{_qt4_bindir}/btscanner
%{_qt4_bindir}/bttennis
%{_qt4_bindir}/calendardemo
%{_qt4_bindir}/camera
%{_qt4_bindir}/cubehouse
%{_qt4_bindir}/declarative-music-browser
%{_qt4_bindir}/dialer_service
%{_qt4_bindir}/documentproperties
%{_qt4_bindir}/flickrdemo
%{_qt4_bindir}/hapticsplayer
%{_qt4_bindir}/hapticsquare
%{_qt4_bindir}/grueapp
%{_qt4_bindir}/landmarkbrowser
%{_qt4_bindir}/logfilepositionsource
%{_qt4_bindir}/mapsdemo
%{_qt4_bindir}/mediabrowser
%{_qt4_bindir}/metadata
%{_qt4_bindir}/metadata2
%{_qt4_bindir}/moreplaces.lmx
%{_qt4_bindir}/mylm.lmx
%{_qt4_bindir}/ndefeditor
%{_qt4_bindir}/nmealog.txt
%{_qt4_bindir}/orientation
%{_qt4_bindir}/places.gpx
%{_qt4_bindir}/publish-subscribe
%{_qt4_bindir}/qml_battery
%{_qt4_bindir}/qml_battery2
%{_qt4_bindir}/qml_camera
%{_qt4_bindir}/qml_device
%{_qt4_bindir}/qml_landmarkmap
%{_qt4_bindir}/qml_location_flickr
%{_qt4_bindir}/qml_mapviewer
%{_qt4_bindir}/qml_networkinfo
%{_qt4_bindir}/qml_poster
%{_qt4_bindir}/qml_scanner
%{_qt4_bindir}/qml_storageinfo
%{_qt4_bindir}/qml_tennis
%{_qt4_bindir}/qmldialer
%{_qt4_bindir}/qmlnotes
%{_qt4_bindir}/qmlorganizer
%{_qt4_bindir}/qsysinfo
%{_qt4_bindir}/qsystemalignedtimer
%{_qt4_bindir}/radio
%{_qt4_bindir}/samplephonebook
%{_qt4_bindir}/sensor_explorer
%{_qt4_bindir}/servicebrowser
%{_qt4_bindir}/sfw-notes
%{_qt4_bindir}/sfwecho_client
%{_qt4_bindir}/sfwecho_service
%{_qt4_bindir}/show_acceleration
%{_qt4_bindir}/show_als
%{_qt4_bindir}/show_compass
%{_qt4_bindir}/show_gyroscope
%{_qt4_bindir}/show_light
%{_qt4_bindir}/show_magneticflux
%{_qt4_bindir}/show_orientation
%{_qt4_bindir}/show_proximity
%{_qt4_bindir}/show_reflectance
%{_qt4_bindir}/show_rotation
%{_qt4_bindir}/show_tap
%{_qt4_bindir}/simplelog.txt
%{_qt4_bindir}/slideshow
%{_qt4_bindir}/todo
%{_qt4_bindir}/videographicsitem
%{_qt4_bindir}/videowidget
%{_qt4_bindir}/xmldata/*.xml
%{_qt4_plugindir}/serviceframework/libserviceframework_bluetoothtransferplugin.so
%{_qt4_plugindir}/serviceframework/libserviceframework_filemanagerplugin.so
%{_qt4_plugindir}/serviceframework/libserviceframework_landlinedialerservice.so
%{_qt4_plugindir}/serviceframework/libserviceframework_notesmanagerplugin.so
%{_qt4_plugindir}/serviceframework/libserviceframework_voipdialerservice.so
%{_qt4_plugindir}/sensors/libqtsensors_grueplugin.so
%endif

%if %{with demos}

#--------------------------------------------------------------------

%package demos
Summary:	Qt Mobility Framework demos
Group:		System/X11
Provides:	qt4-mobility-demos = %{version}-%{release}

%description demos
Example files for the Qt Mobility Framework.

%files demos
%defattr(-,root,root,-)
%{_qt4_bindir}/lightmaps_with_location
%{_qt4_bindir}/player
%{_qt4_bindir}/qmlcontacts
%{_qt4_bindir}/smallsensors
%{_qt4_bindir}/weatherinfo_with_location
%endif

#--------------------------------------------------------------------

%prep
%setup -qn %{name}-opensource-src-%{version}
%patch1 -p1 -b .pulseaudio_lib
%patch50 -p1 -b .translationsdir

%build
PATH="%{_qt4_bindir}:$PATH" ; export PATH

./configure \
    -prefix %{_qt4_datadir} \
    -libdir %{_qt4_libdir} \
    -plugindir %{_qt4_plugindir} \
    %{?with_examples:-examples} \
    %{?with_demos:-demos}

%make

%install
%makeinstall INSTALL_ROOT=%{buildroot} 

# install docs
install -d -m 755 %{buildroot}%{_docdir}/html/qtmobility/
cp -a doc/html/* %{buildroot}%{_docdir}/html/qtmobility/

# die rpath, die
chrpath --delete %{buildroot}%{_bindir}/* ||:
chrpath --delete %{buildroot}%{_qt4_libdir}/libQt*.so ||:
chrpath --delete %{buildroot}%{_qt4_plugindir}/*/*.so ||:
chrpath --delete %{buildroot}%{_qt4_importdir}/*/*.so ||:
chrpath --delete %{buildroot}%{_qt4_importdir}/*/*/*.so ||:

