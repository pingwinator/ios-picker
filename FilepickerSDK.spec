Pod::Spec.new do |s|
  s.name         = "FilepickerSDK"
  s.version      = "2.6.1"
  s.summary      = "FPPicker.framework is the Filepicker.io iOS famework."
  s.homepage     = "https://developers.filepicker.io/docs/ios/"
  s.screenshots  = "https://github.com/Filepicker/ios/raw/master/Documenation%20Files/filepicker_ios.png"
  s.license      = { :type => 'MIT', :file => 'license.txt' }

  s.author       = { "Liyan Chang" => "liyan@filepicker.io" }

  s.source       = {
    :git => 'https://github.com/pingwinator/ios-picker.git',
  }

  s.platform     = :ios

  s.source_files = 'FPPicker/*.{h,m}'
  s.frameworks   = 'AssetsLibrary', 'QuartzCore', 'CoreGraphics', 'MobileCoreServices', 'Foundation', 'CoreFoundation'
  s.xcconfig     = { 'FRAMEWORK_SEARCH_PATHS' => '"$(PODS_ROOT)/FilepickerSDK/library"' }

  s.requires_arc = true

  s.resource = "dist/FPPicker.bundle"
end
