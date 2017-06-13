# Copy this file to additional_environment.rb and add any statements
# that need to be passed to the Rails::Initializer.  `config` is
# available in this context.
#
# Example:
#
#   config.log_level = :debug
#   ...
#
config.log_level = :debug
config.paths['log'] = "/var/log/redmine/dez_vi/redmine_production.log"

config.cache_store = :dalli_store, 'localhost', {
  :namespace => 'redmine_dez_vi',
  :expires_in => 1.hour,
  :compress => true,
  :pool_size => 8
}

##RedmineApp::Application.routes.default_scope = '/[u'it', u'it-projekte', u'anwendungsbetreuung', u'it-sicherheit', u'verz']'
#config.after_initialize do
#  Redmine::Utils::relative_url_root = '/[u'it', u'it-projekte', u'anwendungsbetreuung', u'it-sicherheit', u'verz']'
#end
#
