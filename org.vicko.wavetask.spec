%undefine _cmake_in_source_build

Name:           wavetask
Version:        6.6.0
Release:        0
Summary:        Reusable Qt6 QML Task Manager Plugin for Plasma 6
License:        GPL-3.0-only
URL:            https://github.com/vickoc911/org.vicko.wavetask
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-declarative-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kservice-devel
BuildRequires:  kf6-kwindowsystem-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-knotifications-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  libplasma6-devel
BuildRequires:  plasma6-activities-devel
BuildRequires:  plasma6-activities-stats-devel
BuildRequires:  libksysguard6-devel
BuildRequires:  plasma6-workspace-devel
BuildRequires:  kwin6-devel
BuildRequires:  cmake(LibTaskManager)
BuildRequires:  cmake(LibNotificationManager)

%description
Plasmoid wavetask Qt6 QML Task Manager plugin for Plasma 6 environments with zoom.

# Añade esto para satisfacer la dependencia de QML que el propio RPM detecta
Provides:       qt6qmlimport(org.vicko.wavetask.1) = %{version}
Provides:       qt6qmlimport(org.vicko.wavetask) = %{version}

%prep
%autosetup -p1 -n wavetask-%{version}

%build
# Forzamos al compilador a buscar en el directorio de build los headers generados (log_settings.h, etc.)
export CXXFLAGS="%{optflags} -I%{_vpath_builddir}/plugin"

%cmake_kf6 \
    -DBUILD_TESTING=OFF \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%kf6_build

%install
%kf6_install
%fdupes %{buildroot}

%files

%files
# 1. Carpeta del Plugin QML
%dir %{_libdir}/qt6/qml/org/vicko
%{_libdir}/qt6/qml/org/vicko/wavetask/

# 2. El Plasmoide
%{_datadir}/plasma/plasmoids/org.vicko.wavetask/

# 3. La Plantilla de Diseño (Layout Template)
%dir %{_datadir}/plasma/layout-templates
%{_datadir}/plasma/layout-templates/org.vicko.wavetask.panel/

%changelog
