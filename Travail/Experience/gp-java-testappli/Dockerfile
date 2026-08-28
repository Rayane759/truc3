FROM gitlab-registry.insee.fr/kubernetes/images/build/maven-jdk-toolbox:21 AS build

WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -q
COPY src ./src
RUN mvn package -DskipTests -q

FROM gitlab-registry.insee.fr/kubernetes/images/run/java:21-rootless-jre AS runtime
WORKDIR /app
COPY --from=build /app/target/*.jar /usr/local/app.jar  
EXPOSE 8080
ENTRYPOINT ["java", "-XX:InitialRAMPercentage=80.0", "-XX:MaxRAMPercentage=80.0", "-jar", "/usr/local/app.jar"]
