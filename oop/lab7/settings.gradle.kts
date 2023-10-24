rootProject.name = "Lab7"

pluginManagement {
    repositories {
        gradlePluginPortal()

    }
}

dependencyResolutionManagement {
    repositories {
        mavenCentral()
    }
}

plugins {
    id("org.gradle.toolchains.foojay-resolver-convention") version "0.4.0"
}

include("app")
