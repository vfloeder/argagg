Name:           argagg
Version:        0.2.2
Release:        2%{?dist}
Summary:        Simple C++ command line argument/option parser

License:        MIT
URL:            https://github.com/vietjtnguyen/argagg/
Source0:        https://github.com/vietjtnguyen/argagg/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen

%description
This is yet another C++ command line argument/option parser. It was written as
a simple and idiomatic alternative to other frameworks like getopt, Boost
program options, TCLAP, and others. The goal is to achieve the majority of
argument parsing needs in a simple manner with an easy to use API. It operates
as a single pass over all arguments, recognizing flags prefixed by `-` (short)
or `--` (long) and aggregating them into easy to access structures with lots of
convenience functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains the header files for developing applications
that use %{name}.

%package        doc
Summary:        Developer documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    doc
The %{name}-devel package contains the documentation for developing
applications that use %{name}.

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%make_install

%check
ctest -V %{?_smp_mflags}

%files

%files devel
%{_includedir}/*

%files doc
%doc %{_datadir}/doc/%{name}

%changelog
* Mon Feb 13 2017 Viet The Nguyen <vietjtnguyen@gmail.com>
- Fixed License field and doc subpackage description typo

* Sat Feb 11 2017 Viet The Nguyen <vietjtnguyen@gmail.com>
- Updated version to 0.2.2

* Fri Feb 10 2017 Viet The Nguyen <vietjtnguyen@gmail.com>
- Separated documentation into a separate package

* Fri Feb 10 2017 Viet The Nguyen <vietjtnguyen@gmail.com>
- Packaged version 0.2.1

* Mon Jan 30 2017 Viet The Nguyen <vietjtnguyen@gmail.com>
- Added missing files specification for empty parent package

* Sun Jan 29 2017 Viet The Nguyen <vietjtnguyen@gmail.com>
- Initial packaging
