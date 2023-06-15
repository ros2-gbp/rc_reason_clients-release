%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-rc-reason-clients
Version:        0.3.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rc_reason_clients package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-requests
Requires:       ros-iron-geometry-msgs
Requires:       ros-iron-rc-reason-msgs
Requires:       ros-iron-rclpy
Requires:       ros-iron-ros2pkg
Requires:       ros-iron-tf2-msgs
Requires:       ros-iron-visualization-msgs
Requires:       ros-iron-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  ros-iron-geometry-msgs
BuildRequires:  ros-iron-rc-reason-msgs
BuildRequires:  ros-iron-rclpy
BuildRequires:  ros-iron-ros-workspace
BuildRequires:  ros-iron-ros2pkg
BuildRequires:  ros-iron-tf2-msgs
BuildRequires:  ros-iron-visualization-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-iron-ament-copyright
BuildRequires:  ros-iron-ament-flake8
BuildRequires:  ros-iron-ament-pep257
%endif

%description
Clients for interfacing with Roboception reason modules on rc_visard and
rc_cube.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/iron"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Thu Jun 15 2023 ruess <felix.ruess@roboception.de> - 0.3.1-1
- Autogenerated by Bloom

* Mon Jun 05 2023 ruess <felix.ruess@roboception.de> - 0.3.0-1
- Autogenerated by Bloom

* Thu Apr 20 2023 ruess <felix.ruess@roboception.de> - 0.2.1-5
- Autogenerated by Bloom

* Tue Mar 21 2023 ruess <felix.ruess@roboception.de> - 0.2.1-4
- Autogenerated by Bloom

