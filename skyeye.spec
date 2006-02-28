Summary:	SkyEye is an Open Source Simulator for ARM
Summary(pl):	SkyEye jest symulatorem procesora ARM
Name:		skyeye
Version:	1.0.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://download.gro.clinux.org/skyeye/%{name}-%{version}.tar.bz2
# Source0-md5:	f28212bda583fdec6b48540da689977d
Source1:	skyeye.conf
URL:		http://www.skyeye.org
BuildRequires:	gtk+2-devel
BuildRequires:	pkg-config
BuildRequires:	atk-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SkyEye is an Open Source Simulator, which can simulate Atmel AT91, 
EP7312, cs89712, StrongARM(SA1100/SA1110), XScale PXA25x. 
Users can run Operating Systems such as Linux, uCLinux, uC/OS-II 
for ARM and can analyze or debug in source level.

%description -l pl
SkyEye jest symulatorem o otwartych �r�d�ach. Symuluje nast�puj�ce 
procesory: Atmel AT91, EP7312, cs89712, StrongARM(SA1100/SA1110), 
XScale PXA25x. Umo�liwia uruchomienie system�w operacyjnych
takich jak Linux, uCLinux, uC/OS-II na procesorze ARM, ich
analiz� i odpluskiwanie na poziomie kodu �r�d�owego.

%prep
%setup -q
install %{SOURCE1} .

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install binary/skyeye $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README skyeye.conf
%attr(755,root,root) %{_bindir}/skyeye
