Summary:	SkyEye - an Open Source Simulator for ARM
Summary(pl.UTF-8):	SkyEye - symulator procesora ARM
Name:		skyeye
Version:	1.0.0
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://download.gro.clinux.org/skyeye/%{name}-%{version}.tar.bz2
# Source0-md5:	f28212bda583fdec6b48540da689977d
Source1:	skyeye.conf
URL:		http://www.skyeye.org/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SkyEye is an Open Source Simulator, which can simulate Atmel AT91,
EP7312, cs89712, StrongARM (SA1100/SA1110), XScale PXA25x. Users can
run Operating Systems such as Linux, uCLinux, uC/OS-II for ARM and can
analyze or debug in source level.

%description -l pl.UTF-8
SkyEye jest symulatorem o otwartych źródłach. Symuluje następujące 
procesory: Atmel AT91, EP7312, cs89712, StrongARM (SA1100/SA1110), 
XScale PXA25x. Umożliwia uruchomienie systemów operacyjnych
takich jak Linux, uCLinux, uC/OS-II na procesorze ARM, ich
analizę i odpluskiwanie na poziomie kodu źródłowego.

%prep
%setup -q
install %{SOURCE1} .

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DSTANDALONE -DDEFAULT_INLINE=0 -DMODET \$(SIM_EXTRA_CFLAGS) -I. `pkg-config --cflags gtk+-2.0`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install binary/skyeye $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README skyeye.conf
%attr(755,root,root) %{_bindir}/skyeye
