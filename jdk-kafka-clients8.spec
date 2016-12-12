Name     : jdk-kafka-clients8
Version  : 0.8.2.1
Release  : 1
URL      : http://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.jar
Source0  : http://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.jar
Source1  : http://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-kafka-clients8-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-kafka-clients8 package.
Group: Data

%description data
data components for the jdk-kafka-clients8 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/kafka-clients8.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/kafka-clients8.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/kafka-clients8.xml \
%{buildroot}/usr/share/maven-poms/kafka-clients8.pom \
%{buildroot}/usr/share/java/kafka-clients8.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/kafka-clients8.jar
/usr/share/maven-metadata/kafka-clients8.xml
/usr/share/maven-poms/kafka-clients8.pom
