plugins {
    id("java")
    application
}

application {
    mainClass.set("Lab7.App")
}

repositories {
    mavenCentral()
}

dependencies {
    // testImplementation("org.junit.jupiter:junit-jupiter:5.9.3")
    // testRuntimeOnly("org.junit.platform:junit-platform-launcher")
    // implementation("com.google.guava:guava:32.1.1-jre")
    implementation("com.google.code.gson:gson:2.10.1")
}



// Apply a specific Java toolchain to ease working on different environments.
java {
    toolchain.languageVersion.set(JavaLanguageVersion.of(17))
}


tasks.withType<Jar>() {
    manifest {
        attributes["Main-Class"] = "Lab7.App"
    }
    configurations["compileClasspath"].forEach { file: File ->
        from(zipTree(file.absoluteFile))
    }
}

// tasks.named<Test>("test") {
//     // Use JUnit Platform for unit tests.
//     useJUnitPlatform()
// }
