<template>
    <nav class="bg-gray-800 p-4">
        <div class="container mx-auto flex items-center justify-between">
            <div>
                <a href="/" class="text-white text-lg font-semibold">LibraryApp</a>
            </div>
            <div>
                <ul class="flex space-x-4">
                    <li><router-link to="/books" class="text-white">Books</router-link></li>
                    <li><router-link to="/members" class="text-white">Members</router-link></li>
                </ul>
            </div>
            <div>
                <input type="text" placeholder="Search..." class="rounded-md p-2" />
            </div>
            <div>
                <router-link to="/help" class="text-white">Help</router-link>
            </div>
        </div>
    </nav>
</template>
