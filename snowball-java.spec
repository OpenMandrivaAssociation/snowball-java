%bcond_with javadoc

Name:          snowball-java
Version:       0
Release:       0.3.20130902.1
Summary:       Java stemming algorithm library
License:       BSD
URL:           https://snowball.tartarus.org/index.php
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

BuildArch:     noarch
BuildSystem:	maven
BuildOption(install):	--file-name %{name}

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

%if %{with javadoc}
%package javadoc
Summary:       Javadoc for %{name}

%endif
%if %{with javadoc}
%description javadoc
This package contains javadoc for %{name}.

%endif
%prep
%setup -q -n libstemmer_java

%patch 0 -p0

cp -p %{SOURCE1} pom.xml
sed -i "s|@VERSION@|%{version}|" pom.xml

cp -p %{SOURCE2} notice.txt
cp -p %{SOURCE3} license.txt
sed -i 's/\r//' license.txt notice.txt

%files -f .mfiles
%doc license.txt notice.txt

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc
%doc license.txt notice.txt

%endif
