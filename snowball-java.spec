%{?_javapackages_macros:%_javapackages_macros}

Name:          snowball-java
Version:       0
Release:       0.3.20130902%{?dist}
Summary:       Java stemming algorithm library
License:       BSD
URL:           http://snowball.tartarus.org/index.php
Source0:       http://snowball.tartarus.org/dist/libstemmer_java.tgz
# Custom pom file
Source1:       snowball-template-pom.xml
# http://snowball.tartarus.org/license.php
Source2:       snowball-notice.txt
# see http://snowball.tartarus.org/license.php
# http://www.opensource.org/licenses/bsd-license.html
Source3:       snowball-BSD-license.txt
# Build fix remove 'break;' 
Patch0:        snowball-remove-unreachable-statement.patch

BuildRequires: java-devel
BuildRequires: maven-local
BuildArch:     noarch

%description
Snowball is a small string processing language
designed for creating stemming algorithms
for use in Information Retrieval.

This package contains all you need to include the
snowball stemming algorithms into a Java
project of your own. If you use this,
you don't need to use the snowball compiler,
or worry about the internals of the
stemmers in any way.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n libstemmer_java

%patch0 -p0

cp -p %{SOURCE1} pom.xml
sed -i "s|@VERSION@|%{version}|" pom.xml

cp -p %{SOURCE2} notice.txt
cp -p %{SOURCE3} license.txt
sed -i 's/\r//' license.txt notice.txt

%build

%mvn_file : %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc license.txt notice.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.txt

%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20130902
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 0-0.2.20130902
- Use Requires: java-headless rebuild (#1067528)

* Mon Sep 02 2013 gil cattaneo <puntogil@libero.it> 0-0.1.20130902
- initial rpm
